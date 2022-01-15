from django.urls import path

from .views import BlogDetailView, BlogsView, HomeView

app_name = "blog"

urlpatterns = [
    path("", HomeView.as_view(), name="index"),
    path("blogs/", BlogsView.as_view(), name="blogs"),
    path("<int:pk>/", BlogDetailView.as_view(), name="blog-detail"),
]
