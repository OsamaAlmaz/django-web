from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, redirect
from .models import Tweets
from .form import TweetForm
import random
from django.utils.http import is_safe_url
from django.conf import settings
from django.views.decorators.csrf import csrf_protect


# Create your views here.

def home_page(request, *args, **kwargs):
    return render(request, template_name="pages/home.html", context={}, status=200)

#this is an inner API that 
ALLOWED_HOSTS = settings.ALLOWED_HOSTS
def tweet_list_view(request, *args, **kwargs):
    """
        REST API
        MUST BE FIRST INITIALIZED BY THE URL TAB IN ORDER FOR THIS TO WORK PROBERLY. 
        getting it from the database.
        consume by Javascript, or other apps.
    """
    print("This the Tweet request:", request.POST)
    qs = Tweets.objects.all()
    tweet_list = [{"id": x.id, "content": x.content, "likes": random.randint(0,100)} for x in qs]
    data = {
        "response": tweet_list
    }
    return JsonResponse(data)

@csrf_protect
def tweet_create_view(request, *args, **kwargs):
    form = TweetForm(request.POST or None)
    print(request.GET.get("next") or None)
    next_url = request.POST.get('next') or None
    print('next url is the following', next_url)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        print(request.is_ajax(), "this is the ajax method")
        if request.is_ajax():
            return JsonResponse({}, status=201)
        
        print(is_safe_url(next_url, ALLOWED_HOSTS))
        if next_url != None and is_safe_url(next_url, ALLOWED_HOSTS):
            return redirect(next_url)
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
