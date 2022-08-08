from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
	title = models.CharField(max_length=128)
	slug = models.CharField(max_length=128, unique=True)
	icon = models.FileField(upload_to="category/")
	post_count = models.IntegerField(default=0)


class Province(models.Model):
	title = models.CharField(max_length=128)
	slug = models.CharField(max_length=128, unique=True)


class Post(models.Model):
	title = models.CharField(max_length=128, verbose_name='Nomi')
	slug = models.CharField(max_length=128, unique=True)
	content = models.TextField()
	sub_content = models.CharField(max_length=128)
	image = models.ImageField(upload_to="post/", null=True)

	author = models.ForeignKey(
		User, on_delete=models.CASCADE, related_name='posts')
	category = models.ForeignKey(
		Category, on_delete=models.SET_NULL, null=True, related_name='posts')
	tags = models.ManyToManyField(Province, related_name='posts')

	published_date = models.DateField(null=True)
	views_count = models.PositiveIntegerField(default=0)

	is_popular = models.BooleanField(default=False)
	is_feature = models.BooleanField(default=False)
    