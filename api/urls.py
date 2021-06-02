
from django.urls import path

from .views import ListCreateAPIView


urlpatterns = [
    path('posts', ListCreateAPIView.as_view(), name='post-list-new'),
]
