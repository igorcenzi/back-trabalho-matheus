from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from tables.serializers import HallTablesSerializer
from tables.models import HallTables
class HallTablesListCreate(generics.ListCreateAPIView):
    queryset = HallTables.objects.all().order_by('table_number')
    serializer_class = HallTablesSerializer
    pagination_class = None
    
    def perform_create(self, serializer):
        capacity = serializer.validated_data.get('capacity')
        instance = serializer.save(seats=0)
        instance.save()


class SetTableUnavailable(APIView):
    def patch(self, request, table_id):
        table = get_object_or_404(HallTables, id=table_id)
        

        people_count = request.data.get('people_count')
        if people_count is None:
            return Response(
                {"error": "people_count is required"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            people_count = int(people_count)
            if people_count <= 0:
                return Response(
                    {"error": "people_count must be a positive integer"}, 
                    status=status.HTTP_400_BAD_REQUEST
                )

            
        except (ValueError, TypeError):
            return Response(
                {"error": "people_count must be a valid integer"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        table.is_available = False
        table.seats = people_count
        if people_count > table.capacity:
            table.capacity = people_count
        table.save()
        
        serializer = HallTablesSerializer(table)
        return Response(serializer.data)


class SetTableAvailable(APIView):
    def patch(self, request, table_id):
        table = get_object_or_404(HallTables, id=table_id)
        
        table.seats = 0
        table.is_available = True
        table.current_session += 1
        table.save()
        
        serializer = HallTablesSerializer(table)
        return Response(serializer.data)

