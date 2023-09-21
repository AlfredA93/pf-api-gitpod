"""Tests for Posts Model"""
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Post


class PostListViewTests(APITestCase):
    """Post List Tests"""
    def setUp(self):
        """Setup for the tests in this class"""
        User.objects.create_user(username='tim', password='qwerty123')

    def test_can_list_posts(self):
        """
        Test List
        # 1. Get the User
        # 2. Create a post with the user, Tim
        # 3. Test the response when requesting an url.
        # 4. Is the response equal to 200 OK?
        """
        tim = User.objects.get(username='tim')  # 1
        Post.objects.create(owner=tim, title='test title')  # 2
        response = self.client.get('/posts/')  # 3
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # 4

    def test_logged_in_user_can_create_post(self):
        """
        Logged In Post Creation Test
        # 1. Login as Tim
        # 2. Make a request to posts url, create a post
        # 2.5 Must have the required fields filled for serializer to validate
        # 3. Count all the posts in 'posts/'
        # 4. Test if it is equal to 1
        # 5. Test if response code is 201_CREATED
        """
        self.client.login(username='tim', password='qwerty123')  # 1
        response = self.client.post('/posts/', {  # 2
            'title': 'a title',
            'summary': 'test summary',  # 2.5
            })
        count = Post.objects.count()  # 3
        self.assertEqual(count, 1)  # 4
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # 5

    def test_user_logged_in_to_post(self):
        """Test User must be logged in to post"""
        response = self.client.post('/posts/', {'title': 'title2'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
