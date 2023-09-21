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


class PostDetailTests(APITestCase):
    """Post Detail View Tests"""
    def setUp(self):
        """
        Data setup for this class of Tests
        # 1. Create Users
        # 2. Create post by each user
        """
        harry = User.objects.create_user(
            username='harry', password='pass123')  # 1
        sally = User.objects.create_user(
            username='sally', password='pass987')  # 1
        Post.objects.create(  # 2
            owner=harry,
            title='Harry travelling',
            summary='Harry travel summary',
            content='Harry content',
        )
        Post.objects.create(  # 2
            owner=sally,
            title='Sally travelling',
            summary='Sally travel summary',
            content='Sally content',
        )

    def test_can_retrieve_post_using_valid_id(self):
        """
        Test retrieve post
        # 1. View the post detail
        # 2. Test Title data
        # 3. Test status code
        """
        response = self.client.get('/posts/1/')  # 1
        self.assertEqual(response.data['title'], 'Harry travelling')  # 2
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # 3

    def test_page_not_found_invalid_post(self):
        """Retrieve data with invalid id"""
        response = self.client.get('/posts/123456789/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_post(self):
        """
        User can update own post
        # 1. User Login
        # 2. Put request to update post with data
        # 3. Test the title is the same as put request
        # 4. Test the status code of update request is 200 OK
        """
        self.client.login(username='harry', password='pass123')  # 1
        response = self.client.put('/posts/1/', {  # 2
            'title': 'Harry goes walking',
            'summary': 'Harry summary editted'
            })
        post = Post.objects.filter(pk=1).first()
        self.assertEqual(post.title, 'Harry goes walking')  # 3
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # 4

    def test_user_cant_update_other_users_post(self):
        """
        User cant update other users posts
        # 1. User Login
        # 2. Put request to update data of post not owned by User
        # 3. Test the HTTP response is FORBIDDEN
        """
        self.client.login(username='harry', password='pass123')  # 1
        response = self.client.put('/posts/2/', {  # 2
            'title': 'Harry edits Sallys post',
            'summary': 'Harry edits Sallys summary'
            })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  # 3
