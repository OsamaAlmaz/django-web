from django.db import models
import random
from django.conf import settings
# Create your models here.
User = settings.AUTH_USER_MODEL

class Tweets(models.Model):
    user = models.ForeignKey (User, on_delete=models.CASCADE)
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
