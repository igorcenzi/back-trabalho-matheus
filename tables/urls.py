from django.contrib import admin
from django.urls import path
from tables import views

urlpatterns = [
    path('tables/', views.HallTablesListCreate.as_view()),
]