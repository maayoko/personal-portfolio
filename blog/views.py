from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.http.request import HttpRequest
from django.urls import reverse

from blog.forms import AddCommentForm

from .models import Blogger, Post, Comment


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_comments"] = Comment.objects.filter(
            post__id=context["post"].id).order_by("published_at")
        return context


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


class CommentView(generic.CreateView):
    template_name = "blog/comment.html"
    # model = Comment
    # fields = ["description"]

    # def get_success_url(self) -> str:
    #     return self.request.META.get('HTTP_REFERER', self.request.path)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["post"] = Post.objects.get(id=self.kwargs.get("pk"))
    #     return context

    def get(self, request: HttpRequest, *args: str, **kwargs):
        if not request.user.is_authenticated:
            return redirect(reverse("login"))

        post = get_object_or_404(Post, pk=kwargs.get("pk"))
        context = {
            "form": AddCommentForm(),
            "post": post
        }
        return render(request, self.template_name, context=context)

    def post(self, request: HttpRequest, *args: str, **kwargs):
        form = AddCommentForm(request.POST)
        post = get_object_or_404(Post, pk=kwargs.get("pk"))

        if form.is_valid():
            comment = Comment()
            comment.title = "New comment"
            comment.description = form.cleaned_data["description"]
            comment.post = post
            comment.save()

            return redirect(reverse("blog:blog-detail", args=(post.id, )))

        context = {
            "form": form,
            "post": post
        }
        return render(request, self.template_name, context=context)
