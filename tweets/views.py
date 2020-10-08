from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, redirect
from tweets.models import Tweets
from .form import TweetForm
from .serializers import (
    TweetSerializer,
    TweetActionSerializer,
    TweetCreateSerializer
)
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view,permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


import random
from django.utils.http import is_safe_url
from django.conf import settings

# Create your views here.
0
def home_page(request, *args, **kwargs):
    return render(request, template_name="pages/home.html", context={}, status=200)

ALLOWED_HOSTS = settings.ALLOWED_HOSTS

@api_view(['GET'])
def tweet_list_view(request, *args, **kwargs):
    qs = Tweets.objects.all()
    serializer = TweetSerializer(qs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def tweet_detail_view(request, tweet_id, *args, **kwargs):
    qs = Tweets.objects.filter(id= tweet_id)
    if not qs.exists():
        return Response({"message": "The Tweet does not exists! Please find another tweet"}, status=404)
    obj = qs.first()
    #how would you serialize the tweet.
    serializer = TweetSerializer(obj)
    return Response(serializer.data, status=200)

@api_view(['POST']) #http method that the client sent are post.
@permission_classes([IsAuthenticated])
def tweet_create_view(request, *args, **kwargs):
    print(request.data, request.POST)
    data = request.POST or None
    serializer = TweetCreateSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data, status=201)
    return Response({}, status=400)

def testing(request, *args, **kwargs):
    qsall= Tweets.objects.all
    return


@api_view(['POST']) #http method that the client sent are post.
@permission_classes([IsAuthenticated])
def tweet_action_view(request, *args, **kwargs):
    '''
    id is required.
    Action: Like, unlike and retweet.
    '''
    print(request.POST, request.data)
    serializer = TweetActionSerializer(data=request.data)
    print(serializer.is_valid())
    print(serializer.validated_data, "this is the validated data")
    if serializer.is_valid(raise_exception=True):
        data = serializer.validated_data
        tweet_id = int(data.get('id'))
        action = data.get('action')
        content = data.get('content')
        qsall= Tweets.objects.all()
        print("start printing all objects",qsall)
        for item in qsall:
            print(item)
        qs = Tweets.objects.filter(id=data.get('id'))
        if not qs.exists():
            return Response({"message": "The specific like does not exists"}, status=404)
        obj = qs.first()
        if action == 'like':
            obj.likes.add(request.user)
        elif action == 'unlike':
            obj.likes.remove(request.user)
        elif action =='retweet':
            parent_obj = obj
            newTweet = Tweets.objects.create(
                user=request.user,
                parent=parent_obj,
                content=content,
            )
            serializer = TweetSerializer(newTweet)
            return Response(serializer.data, status=200)
    return Response({"message": "likes is added now."}, status=200)


@api_view(['DELETE','GET', 'POST'])
@permission_classes([IsAuthenticated])
def tweet_delete_view(request, tweet_id, *args, **kwargs):
    is_tweet = Tweets.objects.filter(id=tweet_id).exists()
    if not is_tweet:
        return Response({"message": "The Tweet does not exists"}, status=404)

    is_user = Tweets.objects.filter(user=request.user).exists()
    print(is_user)
    if not is_user:
        return Response({'message': 'user is not Registered! Please register and Delete the Tweet'}, status=401)
    if not is_tweet:
        return Response({"message":"User or Tweet id is not registered"},status=404)
    print(is_tweet)

    qs = Tweets.objects.filter(id=tweet_id).delete()
    return Response( {'message': 'Tweet was successfully deleted!'}, status=200)


def tweet_list_view_1(request, *args, **kwargs):
    """
        REST API
        MUST BE FIRST INITIALIZED BY THE URL TAB IN ORDER FOR THIS TO WORK PROBERLY.
        getting it from the database.
        consume by Javascript, or other apps.
    """
    qs = Tweets.objects.all()
    tweet_list = [x.searlize() for x in qs]
    data = {
        "response": tweet_list
    }
    return JsonResponse(data)




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
