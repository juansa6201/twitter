from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.urls import reverse_lazy
# Create your models here.
class Tweet(models.Model):
    message = models.CharField('Texto', max_length=142)
    datetime = models.DateTimeField('Fecha',auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    user.verbose_name='Usuario'

    def __str__(self):
        return 'Tweet nro {} - by {}'.format(self.id, self.user)


class ReTweet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    tweet = models.ForeignKey(Tweet, related_name='my_retuits')
    comment = models.CharField(max_length=143)

    def __str__(self):
        return 'Retweet de '.format(self.tweet)


class Likes(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    tweet = models.ForeignKey(Tweet, related_name='my_likes')

    def __str__(self):
        return 'Like de {}'.format(self.user)

    class Meta:
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'
