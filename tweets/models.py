from django.db import models
import random
from django.conf import settings
# Create your models here.
User = settings.AUTH_USER_MODEL

class TweetLike(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    tweet = models.ForeignKey("Tweets", on_delete=models.CASCADE)


class Tweets(models.Model):
    user = models.ForeignKey (User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='tweet_user', blank=True, through=TweetLike)
    content = models.TextField(null=True, blank=True)
    image = models.FileField(upload_to= 'image/', blank= True, null= True)

    class Meta:
        ordering = ['-id']

    def searlize(self):
        return{
            "id": self.id,
            "content": self.content,
            "likes": random.randint(0,200)
        }
