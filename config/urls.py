"""twitter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from twitter import views as core_views
from twitter.views import (dame_tuits, post_tweet, user, activate)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', dame_tuits, name='$'),
    url(r'^twitear/', post_tweet, name='twitear'),
    url(r'^eliminar_tweet/', core_views.eliminar_tweet, name='eliminar_tweet'),
    url(r'^login/', auth_views.login, name='login'),
    url(r'^logout/', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^signup/', core_views.signup, name='signup'),
    url(r'^retuit/(?P<tweet_id>[0-9]+)/$', core_views.retuit, name='retuit'),
    url(r'^retuit_user/(?P<tweet_id>[0-9]+)/$', core_views.retuit_user, name='retuit_user'),
    url(r'^liked/(?P<tweet_id>[0-9]+)/$', core_views.liked, name='liked'),
    url(r'^liked_user/(?P<tweet_id>[0-9]+)/$', core_views.liked_user, name='liked_user'),
    url(r'^user/', user, name='user'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        activate, name='activate'),

]
