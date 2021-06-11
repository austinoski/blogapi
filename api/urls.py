
from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token

from .views import ListCreateAPIView, PostPublishAPIView, RetrieveUpdateAPIView
from .views import UserCreateAPIView, UserRetrieveDeleteAPIView


urlpatterns = [
    path('post', ListCreateAPIView.as_view(), name='post-list-new'),
    path('post/<int:pk>/publish', PostPublishAPIView.as_view(), name='post-publish'),
    path('post/<int:pk>', RetrieveUpdateAPIView.as_view(), name='post-retrieve-update'),

    path('user', UserCreateAPIView.as_view(), name='user-new'),
    path('user/<int:pk>', UserRetrieveDeleteAPIView.as_view(), name='user-retrieve-delete'),
    path('user/token', obtain_auth_token, name='token-retrieve'),
]
