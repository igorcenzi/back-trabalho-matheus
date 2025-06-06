# Generated by Django 5.2 on 2025-06-04 01:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('additionals', '0001_initial'),
        ('products', '0001_initial'),
        ('tables', '0002_halltables_capacity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pendente', 'Pendente'), ('finalizado', 'Finalizado'), ('cancelado', 'Cancelado')], default='pendente', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='tables.halltables')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('notes', models.TextField(blank=True, null=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.product')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItemAdditional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('additional', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='additionals.additional')),
                ('order_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='additionals_items', to='orders.orderitem')),
            ],
        ),
    ]
