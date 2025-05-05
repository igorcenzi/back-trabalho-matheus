from django.contrib import admin
from django.urls import path
from authentication.views import UserList
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

urlpatterns = [
    path('user/', UserList.as_view(), name='create_user'),
    path('user/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]