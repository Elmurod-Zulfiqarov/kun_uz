from django.urls import path

from .views import (
	PostListView, CategoryListView, ProvinceListView,
	ResentlyPostListView, FeaturePostListView
)


urlpatterns = [
	path("api/v1/post/", PostListView.as_view(), name="post"),
	path("api/v1/post/resently/", ResentlyPostListView.as_view(), name="post_resently"),
	path("api/v1/post/featured/", FeaturePostListView.as_view(), name="post_feature"),
	path("api/v1/category/", CategoryListView.as_view(), name="category"),
	path("api/v1/province/", ProvinceListView.as_view(), name="tag")	
]
