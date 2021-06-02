
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers, status

from .serializers import PostSerializer
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
