from django.db import models

# Create your models here.

class Tweets(models.Model):
    content = models.TextField(null=True, blank=True)
    image = models.FileField(upload_to= 'image/', blank= True, null= True)