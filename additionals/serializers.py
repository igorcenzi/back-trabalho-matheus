from rest_framework import serializers
from additionals.models import Additional
from products.serializers import ProductSerializer

class AdditionalSerializer(serializers.ModelSerializer):
    products_details = ProductSerializer(source='products', many=True, read_only=True)
    
    class Meta:
        model = Additional
        fields = '__all__'
