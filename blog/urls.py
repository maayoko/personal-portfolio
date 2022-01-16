from django.urls import path

from .views import BlogDetailView, BloggerView, BloggersView, BlogsView, CommentView, HomeView

app_name = "blog"

urlpatterns = [
    path("", HomeView.as_view(), name="index"),
    path("blogs/", BlogsView.as_view(), name="blogs"),
    path("<int:pk>/", BlogDetailView.as_view(), name="blog-detail"),
    path("blogger/<int:pk>/", BloggerView.as_view(), name="blogger"),
    path("bloggers/", BloggersView.as_view(), name="bloggers"),
    path("<int:pk>/create/", CommentView.as_view(), name="comment")
]
