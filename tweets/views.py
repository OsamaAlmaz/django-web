from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render
from .models import Tweets

# Create your views here.

def home_page(request, *args, **kwargs):
    return render(request, template_name="pages/home.html", context={}, status=200)

#this is an inner API that 
def tweet_list_view(request, *args, **kwargs):

    """
        REST API
        consume by Javascript, or other apps.
    """
    
    qs = Tweets.objects.all()
    tweet_list = [{"id": x.id, "content": x.content} for x in qs]
    data = {
        "response":tweet_list
    }
    return JsonResponse(data)

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
