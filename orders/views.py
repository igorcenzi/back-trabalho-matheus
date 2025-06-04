from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from orders.models import Order
from orders.serializers import OrderSerializer, OrderCreateSerializer, OrderStatusUpdateSerializer
from tables.models import HallTables

class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint para gerenciar pedidos.
    Permite filtrar pedidos por mesa e status.
    """
    queryset = Order.objects.all().order_by('-created_at')
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['table', 'status']
    
    def get_serializer_class(self):
        if self.action == 'create':
            return OrderCreateSerializer
        return OrderSerializer
    
    @action(detail=True, methods=['patch'], url_path='status')
    def update_status(self, request, pk=None):
        """
        Endpoint para atualizar o status do pedido.
        """
        order = self.get_object()
        serializer = OrderStatusUpdateSerializer(order, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(OrderSerializer(order).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TableOrdersListView(generics.ListAPIView):
    """
    API endpoint para listar pedidos de uma mesa específica.
    Retorna apenas os pedidos da sessão atual da mesa.
    """
    serializer_class = OrderSerializer
    
    def get_queryset(self):
        table_id = self.kwargs['table_id']
        table = get_object_or_404(HallTables, id=table_id)
        # Filtra apenas os pedidos da sessão atual da mesa
        return Order.objects.filter(table=table, session=table.current_session).order_by('-created_at')
