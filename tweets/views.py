from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render
from .models import Tweets
from .form import TweetForm
import random

# Create your views here.

def home_page(request, *args, **kwargs):
    return render(request, template_name="pages/home.html", context={}, status=200)

#this is an inner API that 
def tweet_list_view(request, *args, **kwargs):
    """
        REST API
        MUST BE FIRST INITIALIZED BY THE URL TAB IN ORDER FOR THIS TO WORK PROBERLY. 
        getting it from the database.
        consume by Javascript, or other apps.
    """

    qs = Tweets.objects.all()
    tweet_list = [{"id": x.id, "content": x.content, "likes": random.randint(0,100)} for x in qs]
    data = {
        "response":tweet_list
    }
    return JsonResponse(data)
def tweet_create_view(request, *args, **kwargs):
    form = TweetForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        form = TweetForm()
    return render(request, 'components/form.html', context={"form": form})

def another_page(request, tweet_id, *args, **kwargs):
    """

        REST API
        consume by Javascript, or other apps.

    """
    data = {
        "id": tweet_id
    }

    try:
        obj = Tweets.objects.get(id=tweet_id)
        data['content'] = obj.content
        status = 200
    except:
        data['message'] = "Not found"
        status = 404

    return JsonResponse(data, status=status)#json dumps content type='application/json'
