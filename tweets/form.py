from django.forms import ModelForm
from django import forms
from .models import Tweets


MAX_TWEET_LENGTH =200

class TweetForm(ModelForm):
    class Meta:
        model = Tweets
        fields = ['content']

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if (len(content) >=  MAX_TWEET_LENGTH):
            raise forms.ValidationError('This Tweet is too long')
        return content

