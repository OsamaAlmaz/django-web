from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, redirect
from .models import Tweets
from .form import TweetForm
from .serializers import TweetSerializer
from rest_framework.response import Response

import random
from django.utils.http import is_safe_url
from django.conf import settings

# Create your views here.

def home_page(request, *args, **kwargs):
    return render(request, template_name="pages/home.html", context={}, status=200)

ALLOWED_HOSTS = settings.ALLOWED_HOSTS

def tweet_list_view(request, *args, **kwargs):
    """
        REST API
        MUST BE FIRST INITIALIZED BY THE URL TAB IN ORDER FOR THIS TO WORK PROBERLY. 
        getting it from the database.
        consume by Javascript, or other apps.
    """
    print("This the Tweet request:")
    qs = Tweets.objects.all()
    tweet_list = [x.searlize() for x in qs]
    data = {
        "response": tweet_list
    }
    return JsonResponse(data)
def tweet_create_view(request, *args, **kwargs):
    data = request.POST or None
    serializer = TweetSerializer(data=request.POST or None)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data)
    return Response({}, status=400)

def tweet_create_view_1(request, *args, **kwargs):
    form = TweetForm(request.POST or None)
    next_url = request.POST.get('next') or None
    print(form.is_valid())
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        print(request.is_ajax(),"This is the is_ajax request tool")
        if request.is_ajax():
            return JsonResponse(obj.searlize(), status=201)
        print("request.is_ajax", request.is_ajax(), "next_url",next_url)
        if next_url != None and is_safe_url(next_url, ALLOWED_HOSTS):
            return redirect(next_url)
        form = TweetForm()
    if form.errors:
        if request.is_ajax:
            return JsonResponse(form.errors, status=400)
    
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
