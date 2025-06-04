from django.urls import path, include
from rest_framework.routers import DefaultRouter
from additionals import views

router = DefaultRouter()
router.register(r'additionals', views.AdditionalViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
