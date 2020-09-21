from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Tweets
from rest_framework.test import APIClient



User = get_user_model()
# Create your tests here.


class TweetTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username='abc', password='somepassword')
        User.objects.create_user(username='osama', password='somepassword')
    
    def test_user_created(self):
        user= User.objects.get(username='osama')
        self.assertEqual(user.username,'osama')
    
    def test_tweet_created(self):
        user = User.objects.get(username='osama')
        tweet_obj = Tweets.objects.create(content='my first tweet', user=user)
        self.assertEqual(tweet_obj.user, user)
        

    def __get_client(self):
        client= APIClient()
        client.login(username='osama', password='somepassword') 
        return client

    def test_api_login(self):
        client = self.__get_client()
        response = client.get('/api/tweets/')
        self.assertEqual(response.status_code, 200)
    
    # we need to test each API.
    
    # def test_action_like(self):
    #     client = self.__get_client()
    #     response = client.post('/api/tweets/action/', {
    #        'id': 3,
    #        'action': 'like'
    #     }, format='json')
    #     print(response)
    #     self.assertEqual(response.status_code, 200)

    def test_action_retweet(self):
        client = self.__get_client()
        response = client.post('/api/tweets/action', {'id': 54 , "action": 'retweet'}, format= 'json')
        print(response.json())