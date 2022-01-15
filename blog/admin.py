from django.contrib import admin

from .models import Blogger, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Blogger)
class BloggerAdmin(admin.ModelAdmin):
    pass
