from django.contrib import admin
from .models import (Tweet,Likes,ReTweet)




class TweetAdmin(admin.ModelAdmin):

    def likes_counter(self, obj):
        if obj:
            return obj.my_likes.count()

    list_display = ('user','datetime')
    list_filter = ('datetime','user')
    search_fields = ('message',)
    readonly_fields = ('likes_counter','datetime')

admin.site.register(Tweet, TweetAdmin)
admin.site.register(ReTweet)
admin.site.register(Likes)

