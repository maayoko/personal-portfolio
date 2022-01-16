from django.contrib import admin

from .models import Blogger, Category, Post, Comment, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Blogger)
class BloggerAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
