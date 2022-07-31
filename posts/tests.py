from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create(
            username='testuser',
            email='test@test.com',
            password='test'
        )

        cls.post = Post.objects.create(
            author=cls.user,
            title='test title',
            body='test body',
        )

    def testPostModel(self):
        self.assertEqual(self.post.author.username, 'testuser')
        self.assertEqual(self.post.title, 'test title')
        self.assertEqual(self.post.body, 'test body')
        self.assertEqual(str(self.post), 'test title')
