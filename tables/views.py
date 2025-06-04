from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from tables.serializers import HallTablesSerializer
from tables.models import HallTables

# Create your views here.
class HallTablesListCreate(generics.ListCreateAPIView):
    """
    List and create tables. When creating a table, the seats field is initialized to 0 (empty table).
    """
    queryset = HallTables.objects.all()
    serializer_class = HallTablesSerializer
    pagination_class = None
    
    def perform_create(self, serializer):
        # When creating a table, initialize seats to 0 (no people seated)
        capacity = serializer.validated_data.get('capacity')
        instance = serializer.save(seats=0)
        instance.save()


class SetTableUnavailable(APIView):
    """
    Endpoint to set a table as unavailable (is_available = False)
    and record the number of people at the table using the seats field
    """
    def patch(self, request, table_id):
        table = get_object_or_404(HallTables, id=table_id)
        
        # Get the number of people from the request data
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
        
        # Update the table
        table.is_available = False
        table.seats = people_count  # Use seats to indicate the number of people
        if people_count > table.capacity:
            table.capacity = people_count
        table.save()
        
        serializer = HallTablesSerializer(table)
        return Response(serializer.data)


class SetTableAvailable(APIView):
    """
    Endpoint to set a table as available (is_available = True),
    reset the number of people to 0, and increment the session counter
    to ensure previous orders won't be listed in the next session.
    """
    def patch(self, request, table_id):
        table = get_object_or_404(HallTables, id=table_id)
        
        # Reset the number of people to 0
        table.seats = 0
        table.is_available = True
        # Incrementa o contador de sessão para que os pedidos anteriores não sejam mais listados
        table.current_session += 1
        table.save()
        
        serializer = HallTablesSerializer(table)
        return Response(serializer.data)

