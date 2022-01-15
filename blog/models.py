from django.db import models
from django.urls import reverse


class Blogger(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField(default="Bio about blogger.")
    birth_date = models.DateField()

    def get_absolute_url(self):
        return reverse("blog:blogger", args=(self.id, ))

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Post(models.Model):
    title = models.CharField(
        max_length=200, help_text="Enter title of the post")
    content = models.TextField()
    summary = models.CharField(
        max_length=400, help_text="Enter summary of the post")
    author = models.ForeignKey(
        Blogger, on_delete=models.SET_NULL, null=True)

    publish_choices = (
        (0, "Not published"),
        (1, "Published")
    )

    published = models.SmallIntegerField(choices=publish_choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-published_at"]

    def get_absolute_url(self):
        return reverse("blog:blog-detail", args=(self.id,))

    def __str__(self) -> str:
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    posts = models.ManyToManyField(Post, related_name="tags")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    published = models.SmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    posts = models.ManyToManyField(Post, related_name="categories")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
