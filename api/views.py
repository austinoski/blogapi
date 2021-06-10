from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers, status

from .serializers import PostSerializer, UserSerializer
from .models import Post


class ListCreateAPIView(APIView):
    serializer_class = PostSerializer

    def get(self, request, format=None):
        queryset = Post.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostPublishAPIView(APIView):
    serializer_class = PostSerializer

    def get(self, request, pk, format=None):
        post = Post.objects.filter(id=pk).first()

        if post:
            post.published = True
            post.save()
            serializer = self.serializer_class(instance=post)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)


class RetrieveUpdateAPIView(APIView):
    serializer_class = PostSerializer

    def get(self, request, pk, format=None):
        post = Post.objects.filter(id=pk).first()

        if post:
            serializer = self.serializer_class(instance=post)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    def patch(self, request, pk, format=None):
        post = Post.objects.filter(id=pk).first()

        if post:
            serializer = self.serializer_class(post, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)


class UserCreateAPIView(APIView):

    serializer_class = UserSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class UserRetrieveDeleteAPIView(APIView):

    serializer_class = UserSerializer

    def get(self, request, pk, format=None):
        user = User.objects.filter(id=pk).first()

        if user:
            serializer = self.serializer_class(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
