from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from additionals.models import Additional
from additionals.serializers import AdditionalSerializer

class AdditionalViewSet(viewsets.ModelViewSet):
    """
    API endpoint para gerenciar adicionais.
    Permite filtrar adicionais por produto.
    """
    queryset = Additional.objects.all()
    serializer_class = AdditionalSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['products', 'is_available']
