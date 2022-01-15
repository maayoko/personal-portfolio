from django.shortcuts import render
from django.views import generic

from .models import Post


class HomeView(generic.ListView):
    template_name = "blog/index.html"
    queryset = []


class BlogsView(generic.ListView):
    paginate_by = 5
    template_name = "blog/blogs.html"
    context_object_name = "posts"
    model = Post


class BlogDetailView(generic.DetailView):
    template_name = "blog/blog-detail.html"
    context_object_name = "post"
    model = Post
