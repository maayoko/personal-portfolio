from datetime import date, datetime
from django.test import TestCase
from django.contrib.auth.models import User

from ..models import Blogger, Post


def create_or_get_user() -> User:
    try:
        return User.objects.get(username="admin")
    except:
        return User.objects.create(
            username="admin",
            password="weak_password",
            email="admin@example.com"
        )


def create_post() -> Post:
    return Post.objects.create(
        title="Blog title 1",
        content="Content of a blog",
        summary="Summary of the blog",
        author=create_blogger(),
        published=0
    )


def create_blogger() -> Blogger:
    return Blogger.objects.create(
        first_name="John",
        last_name="Doe",
        user=create_or_get_user(),
        email="johndoe@example.com",
        birth_date=date(1988, 7, 17)
    )


class PostModelTests(TestCase):
    def test_model_has_fields(self):
        post = create_post()
        self.assertIsInstance(post.title, str)
        self.assertIsInstance(post.content, str)
        self.assertIsInstance(post.summary, str)
        self.assertIsInstance(post.author.id, int)
        self.assertIsInstance(post.published, int)
        self.assertIsInstance(post.created_at, datetime)
        self.assertIsInstance(post.updated_at, datetime)
        self.assertIsInstance(post.published_at, datetime)


class BloggerModelTests(TestCase):
    def test_model_has_fields(self):
        blogger = create_blogger()
        self.assertIsInstance(blogger.first_name, str)
        self.assertIsInstance(blogger.last_name, str)
        self.assertIsInstance(blogger.email, str)
        self.assertIsInstance(blogger.birth_date, date)
