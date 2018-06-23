# -*- coding: utf-8 -*-
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import EmailMessage
from django.db import IntegrityError
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils import timezone
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from twitter.models import Likes
from twitter.models import ReTweet
from twitter.models import Tweet

from .forms import *
from .tokens import account_activation_token


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
        'retuits': ReTweet.objects.filter(user=request.user),
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

    return render(request, 'twitear.html', {'form': form})


def signup(request):
    try:
        if request.method == 'POST':
            form = SignUpForm(request.POST)

            if form.is_valid():
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                current_site = get_current_site(request)
                mail_subject = 'Activa tu cuenta de Twitter'
                message = render_to_string('registration/acc_active_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                })
                to_email = form.cleaned_data.get('email')
                email = EmailMessage(
                    mail_subject, message, to=[to_email]
                )
                email.send()
                return HttpResponse('Por favor, confirme su dirección de correo electrónico para completar el registro')
        else:
            form = SignUpForm()
        return render(request, 'registration/signup.html', {'form': form})
    except IntegrityError:
        return HttpResponse('<head>'
                            '<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css"integrity="sha384-WskhaSGFgHYWDcbwN70/dfYBj47jz9qbsMId/iRN3ewGhXQFZCSftd1LZCfmhktB" crossorigin="anonymous">'
                            '</head>'+'<div style="text-align: center">''<br>''<p style="color: red">El email que introduciste ya esta en uso</p>''<br>''<a class="btn btn-primary" href="/signup/">Vovler a registrarse</a>'+'</div>')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        return HttpResponseRedirect("../../../login/")
    else:
        return HttpResponse('Link de activacion invalido!')


def retuit(request, tweet_id):
    tuit = Tweet.objects.get(id=tweet_id)
    try:
        retweet = ReTweet.objects.get(user=request.user, tweet=tuit)
        retweet.delete()
    except ObjectDoesNotExist:
        retweet = ReTweet(user=request.user, tweet=tuit)
        retweet.save()

    return HttpResponseRedirect("/")

def retuit_user(request, tweet_id):
    tuit = Tweet.objects.get(id=tweet_id)
    try:
        retweet = ReTweet.objects.get(user=request.user, tweet=tuit)
        retweet.delete()
    except ObjectDoesNotExist:
        retweet = ReTweet(user=request.user, tweet=tuit)
        retweet.save()

    return HttpResponseRedirect("../../user/")

def liked(request, tweet_id):
    tuit = Tweet.objects.get(id=tweet_id)
    try:
        like = Likes.objects.get(user=request.user, tweet=tuit)
        like.delete()
    except ObjectDoesNotExist:
        like = Likes(user=request.user, tweet=tuit)
        like.save()

    return HttpResponseRedirect("/")

def liked_user(request, tweet_id):
    tuit = Tweet.objects.get(id=tweet_id)
    try:
        like = Likes.objects.get(user=request.user, tweet=tuit)
        like.delete()
    except ObjectDoesNotExist:
        like = Likes(user=request.user, tweet=tuit)
        like.save()

    return HttpResponseRedirect("../../user/")

def eliminar_tweet(request):
    tuit=Tweet.objects.filter(user=request.user)
    tuit.delete()
    return HttpResponseRedirect("/")
