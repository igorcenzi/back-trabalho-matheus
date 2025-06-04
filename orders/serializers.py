from rest_framework import serializers
from orders.models import Order, OrderItem, OrderItemAdditional
from tables.serializers import HallTablesSerializer
from products.serializers import ProductSerializer
from additionals.serializers import AdditionalSerializer

class OrderItemAdditionalSerializer(serializers.ModelSerializer):
    additional_details = AdditionalSerializer(source='additional', read_only=True)
    
    class Meta:
        model = OrderItemAdditional
        fields = ['id', 'additional', 'additional_details', 'quantity']

class OrderItemSerializer(serializers.ModelSerializer):
    product_details = ProductSerializer(source='product', read_only=True)
    additionals_items = OrderItemAdditionalSerializer(many=True, read_only=True)
    additionals = serializers.PrimaryKeyRelatedField(
        many=True, 
        write_only=True, 
        queryset=OrderItemAdditional.objects.all(),
        required=False
    )
    subtotal = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'product_details', 'quantity', 'notes', 'additionals_items', 'additionals', 'subtotal']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    table_details = HallTablesSerializer(source='table', read_only=True)
    total = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    
    class Meta:
        model = Order
        fields = ['id', 'table', 'table_details', 'status', 'created_at', 'updated_at', 'items', 'total']

class OrderItemCreateSerializer(serializers.ModelSerializer):
    additionals = serializers.ListField(
        child=serializers.DictField(
            child=serializers.IntegerField(),
        ),
        required=False,
        write_only=True
    )
    
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity', 'notes', 'additionals']

class OrderCreateSerializer(serializers.ModelSerializer):
    items = OrderItemCreateSerializer(many=True, write_only=True)
    
    class Meta:
        model = Order
        fields = ['table', 'items']
    
    def create(self, validated_data):
        items_data = validated_data.pop('items')
        table = validated_data.get('table')
        
        # Adiciona a sessão atual da mesa ao pedido
        order = Order.objects.create(
            **validated_data,
            session=table.current_session
        )
        
        for item_data in items_data:
            additionals_data = item_data.pop('additionals', [])
            order_item = OrderItem.objects.create(order=order, **item_data)
            
            for additional_data in additionals_data:
                additional_id = additional_data.get('additional')
                quantity = additional_data.get('quantity', 1)
                OrderItemAdditional.objects.create(
                    order_item=order_item,
                    additional_id=additional_id,
                    quantity=quantity
                )
        
        return order

class OrderStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['status']
