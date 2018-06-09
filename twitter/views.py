
 # -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import AnonymousUser
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from datetime import datetime, timedelta
from django.utils import timezone
from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from twitter.models import Tweet
from twitter.models import ReTweet
from twitter.models import Likes
from .forms import *
from django.core.exceptions import ObjectDoesNotExist

def dame_tuits(request):
    context = {
        'tuits': Tweet.objects.all(),
        'retuits': ReTweet.objects.all(),
        'likes': Likes.objects.all()
    }

    return render(request, 'tweets.html', context)

def user(request):
    context = {
        'tuits': Tweet.objects.filter(user=request.user),
        'retuits': ReTweet.objects.all(),
        'likes': Likes.objects.all()
    }

    return render(request, 'user.html', context)



def post_tweet(request):
    if request.method == "POST":
        form = FormTweet(request.POST)
        if form.is_valid():

            post = form.save(commit=False)
            post.user = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('../')
    else:
        form = FormTweet()

    return render(request, 'twitear.html',{'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('../')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

def retuit(request, tweet_id):
    tuit=Tweet.objects.get(id=tweet_id)
    try:
        retweet= ReTweet.objects.get(user=request.user, tweet=tuit)
        retweet.delete()
    except ObjectDoesNotExist:
        retweet=ReTweet(user=request.user, tweet=tuit)
        retweet.save()

    return HttpResponseRedirect("/")

def liked(request, tweet_id):
    tuit=Tweet.objects.get(id=tweet_id)
    try:
        like= Likes.objects.get(user=request.user, tweet=tuit)
        like.delete()
    except ObjectDoesNotExist:
        like=Likes(user=request.user, tweet=tuit)
        like.save()

    return HttpResponseRedirect("/")
