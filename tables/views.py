from django.shortcuts import render
from rest_framework import generics
from tables.serializers import HallTablesSerializer
from tables.models import HallTables

# Create your views here.
class HallTablesListCreate(generics.ListCreateAPIView):

    queryset = HallTables.objects.all()
    serializer_class = HallTablesSerializer