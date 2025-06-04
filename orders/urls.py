from django.urls import path, include
from rest_framework.routers import DefaultRouter
from orders import views

router = DefaultRouter()
router.register(r'orders', views.OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('tables/<int:table_id>/orders/', views.TableOrdersListView.as_view(), name='table-orders'),
]
