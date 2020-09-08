from django.contrib import admin

# Register your models here.
from .models import Tweets, TweetLike




class TweetAdmin(admin.ModelAdmin):
    list_display = ['__str__','user']
    search_fields = ['content','user__username','user__email']
    class Meta:
        model= Tweets


admin.site.register (Tweets,TweetAdmin)
