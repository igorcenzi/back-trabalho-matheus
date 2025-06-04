import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from additionals.models import Additional
from products.models import Product

# Lista de adicionais para criar
adicionais = [
    {
        "name": "Queijo Extra",
        "description": "Porção extra de queijo",
        "price": 5.00,
        "is_available": True
    },
    {
        "name": "Bacon",
        "description": "Porção de bacon crocante",
        "price": 7.00,
        "is_available": True
    },
    {
        "name": "Cebola Caramelizada",
        "description": "Porção de cebola caramelizada",
        "price": 4.00,
        "is_available": True
    },
    {
        "name": "Molho Especial",
        "description": "Molho da casa",
        "price": 3.00,
        "is_available": True
    },
    {
        "name": "Batata Frita",
        "description": "Porção pequena de batata frita",
        "price": 8.00,
        "is_available": True
    }
]

# Criar os adicionais
for adicional_data in adicionais:
    adicional = Additional.objects.create(**adicional_data)
    print(f"Adicional {adicional.name} criado com ID {adicional.id}")

# Associar adicionais aos produtos
# Vamos associar alguns adicionais aos pratos principais
pratos_principais = Product.objects.filter(category__id=3)
for prato in pratos_principais:
    # Adicionar todos os adicionais aos pratos principais
    for adicional in Additional.objects.all():
        prato.additionals.add(adicional)
    print(f"Adicionais associados ao produto {prato.name}")

print("Todos os adicionais foram criados e associados com sucesso!")
