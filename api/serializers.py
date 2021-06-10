from django.utils import timezone
from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Post


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        writeonly_fields = ['password']
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.save()
        return user


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'
    
    def create(self, validated_data):
        post = Post.objects.create(**validated_data)
        post.save()
        return post
    
    def update(self, instance, validated_data):
        for field in validated_data.keys():
            setattr(instance, field, validated_data[field])
        instance.updated_at = timezone.now()
        return instance
