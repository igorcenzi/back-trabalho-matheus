from django.contrib import admin
from django.urls import path
from tables import views

urlpatterns = [
    path('tables/', views.HallTablesListCreate.as_view()),
    path('tables/<int:table_id>/set-unavailable/', views.SetTableUnavailable.as_view(), name='set-table-unavailable'),
    path('tables/<int:table_id>/set-available/', views.SetTableAvailable.as_view(), name='set-table-available'),
]