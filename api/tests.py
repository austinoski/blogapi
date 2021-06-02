from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient

from .models import Post


class EndpointTestCase(TestCase):
    def setUp(self):
        self.post1 = Post.objects.create(
            title='New Post Title 1', body='Sweet post body 1')
        self.post2 = Post.objects.create(
            title='New Post Title 2', body='Sweet post body 2')
        self.post3 = Post.objects.create(
            title='New Post Title 3', body='Sweet post body 3')
        
        self.client = APIClient()
    
    def test_post_list_endpoint(self):
        response = self.client.get(reverse('post-list-new'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.headers['Content-Type'], 'application/json')
    
    def test_post_create_endpoint(self):
        data = {'title': 'New Post Title 4', 'body': 'Sweet post body 4'}
        response = self.client.post(reverse('post-list-new'), data=data)
        response_data = response.json()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response_data['id'], 4)
        self.assertEqual(response_data['title'], data['title'])
        self.assertEqual(response_data['body'], data['body'])
    
    def test_post_create_endpoint_on_bad_request(self):
        data = {'topic': 'Bad Topic', 'content': 'Bad content'}
        response = self.client.post(reverse('post-list-new'), data=data)
        self.assertEqual(response.status_code, 400)

    def test_publish_post_endpoint(self):
        response = self.client.get(reverse('post-publish', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json()['published'])
    
    def test_post_publish_endpoint_on_bad_request(self):
        response = self.client.get(reverse('post-publish', args=[1000]))
        self.assertEqual(response.status_code, 400)
