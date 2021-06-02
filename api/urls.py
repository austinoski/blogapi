
from django.urls import path

from .views import ListCreateAPIView, PostPublishAPIView


urlpatterns = [
    path('posts', ListCreateAPIView.as_view(), name='post-list-new'),
    path('post/<int:pk>/publish', PostPublishAPIView.as_view(), name='post-publish'),
]
