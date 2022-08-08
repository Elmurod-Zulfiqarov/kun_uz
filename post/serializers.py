from rest_framework.serializers import ModelSerializer
from post.models import Post, Category, Province


class CategorySerializer(ModelSerializer):
	class Meta:
		model = Category
		fields = '__all__'


class ProvinceSerializer(ModelSerializer):
	class Meta:
		model = Province
		fields = '__all__'

	
class PostSerializer(ModelSerializer):
	class Meta:
		model = Post
		fields = '__all__'
		depth = 1
		