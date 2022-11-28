from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post, Comment




class PostSerializer(serializers.ModelSerializer):



    class Meta:
        model = Post
        fields = '__all__'


# class UserSerializer(serializers.ModelSerializer):
#
#
#     class Meta:
#         model = User
#         fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):


    class Meta:
        model = Comment
        fields = "__all__"