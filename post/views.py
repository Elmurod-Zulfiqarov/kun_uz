from .models import Post, Province, Category
from django.views import View
from .serializers import PostSerializer, ProvinceSerializer, CategorySerializer
from rest_framework.generics import ListAPIView


class PostListView(ListAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer


class ResentlyPostListView(ListAPIView):
	queryset = Post.objects.order_by("-published_date")
	serializer_class = PostSerializer


class FeaturePostListView(ListAPIView):
	queryset = Post.objects.filter(is_feature=True)
	serializer_class = PostSerializer


class ProvinceListView(ListAPIView):
	queryset = Province.objects.all()
	serializer_class = ProvinceSerializer


class CategoryListView(ListAPIView):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer

