from django.contrib import admin

from post.models import Category, Post, Province

admin.site.register([Post, Category, Province])
