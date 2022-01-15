from django.shortcuts import render
from django.views import generic

from .models import Blogger, Post


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


class BloggerView(generic.DetailView):
    template_name = "blog/blogger.html"
    context_object_name = "blogger"
    model = Blogger

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["blogger_posts"] = Post.objects.filter(
            author__id=context["blogger"].id).order_by("-published_at")

        print(len(context["blogger_posts"]))
        return context


class BloggersView(generic.ListView):
    template_name = "blog/bloggers.html"
    context_object_name = "bloggers"
    model = Blogger
