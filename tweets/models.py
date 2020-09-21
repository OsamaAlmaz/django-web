from django.db import models
import random
from django.conf import settings
# Create your models here.
User = settings.AUTH_USER_MODEL

#there is the user model here. that had the id and the name.

class TweetLike(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    tweet = models.ForeignKey("Tweets", on_delete=models.CASCADE)
    timestamp= models.DateTimeField(auto_now_add=True)


class Tweets(models.Model):
    parent= models.ForeignKey("self", null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey (User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='tweet_user', blank=True, through=TweetLike)
    content = models.TextField(null=True, blank=True)
    image = models.FileField(upload_to= 'image/', blank= True, null=True)
    timestamp= models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-id']


    @property
    def is_retweet(self):
        return self.parent != None
    

    def searlize(self):

        """
        feel free to delete. 
        """
        return{
            "id": self.id,
            "content": self.content,
            "likes": random.randint(0,200)
        }
