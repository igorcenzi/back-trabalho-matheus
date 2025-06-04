from django.db import models
from tables.models import HallTables
from products.models import Product
from additionals.models import Additional

class Order(models.Model):
    STATUS_CHOICES = (
        ('pendente', 'Pendente'),
        ('finalizado', 'Finalizado'),
        ('cancelado', 'Cancelado'),
    )
    
    table = models.ForeignKey(HallTables, on_delete=models.CASCADE, related_name='orders')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    session = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'Pedido {self.id} - Mesa {self.table.table_number}'
    
    @property
    def total(self):
        total = 0
        for item in self.items.all():
            total += item.subtotal
        return total

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField(default=1)
    notes = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f'{self.quantity}x {self.product.name}'
    
    @property
    def subtotal(self):
        additionals_total = sum(item.additional.price * item.quantity for item in self.additionals_items.all())
        return (self.product.price * self.quantity) + additionals_total

class OrderItemAdditional(models.Model):
    order_item = models.ForeignKey(OrderItem, on_delete=models.CASCADE, related_name='additionals_items')
    additional = models.ForeignKey(Additional, on_delete=models.PROTECT)
    quantity = models.IntegerField(default=1)
    
    def __str__(self):
        return f'{self.quantity}x {self.additional.name}'
