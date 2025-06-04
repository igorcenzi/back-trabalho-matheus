import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from categories.models import Category
from products.models import Product

# Criar produtos para a categoria Bebidas (ID 2)
bebidas = [
    {
        "name": "Água Mineral",
        "description": "Água mineral sem gás 500ml",
        "price": 5.00,
        "is_available": True
    },
    {
        "name": "Refrigerante",
        "description": "Refrigerante lata 350ml",
        "price": 7.50,
        "is_available": True
    },
    {
        "name": "Suco Natural",
        "description": "Suco de laranja, limão ou abacaxi 300ml",
        "price": 9.00,
        "is_available": True
    },
    {
        "name": "Cerveja",
        "description": "Cerveja long neck 355ml",
        "price": 12.00,
        "is_available": True
    }
]

# Criar produtos para a categoria Pratos Principais (ID 3)
pratos_principais = [
    {
        "name": "Filé Mignon",
        "description": "Filé mignon grelhado com molho madeira e batatas",
        "price": 65.00,
        "is_available": True
    },
    {
        "name": "Risoto de Camarão",
        "description": "Risoto cremoso com camarões e ervas frescas",
        "price": 72.00,
        "is_available": True
    },
    {
        "name": "Massa ao Molho Pesto",
        "description": "Espaguete com molho pesto, tomate seco e parmesão",
        "price": 48.00,
        "is_available": True
    }
]

# Criar produtos para a categoria Sobremesas (ID 4)
sobremesas = [
    {
        "name": "Pudim de Leite",
        "description": "Pudim de leite condensado tradicional",
        "price": 15.00,
        "is_available": True
    },
    {
        "name": "Petit Gateau",
        "description": "Bolo de chocolate com centro derretido e sorvete de creme",
        "price": 22.00,
        "is_available": True
    }
]

# Criar produtos para a categoria Entradas (ID 5)
entradas = [
    {
        "name": "Bruschetta",
        "description": "Torradas com tomate, manjericão e azeite",
        "price": 28.00,
        "is_available": True
    },
    {
        "name": "Carpaccio",
        "description": "Finas fatias de carne crua com molho de alcaparras",
        "price": 35.00,
        "is_available": True
    }
]

# Obter categorias
categoria_bebidas = Category.objects.get(id=2)
categoria_pratos = Category.objects.get(id=3)
categoria_sobremesas = Category.objects.get(id=4)
categoria_entradas = Category.objects.get(id=5)

# Adicionar produtos para cada categoria
for produto in bebidas:
    Product.objects.create(category=categoria_bebidas, **produto)
    print(f"Produto {produto['name']} adicionado à categoria Bebidas")

for produto in pratos_principais:
    Product.objects.create(category=categoria_pratos, **produto)
    print(f"Produto {produto['name']} adicionado à categoria Pratos Principais")

for produto in sobremesas:
    Product.objects.create(category=categoria_sobremesas, **produto)
    print(f"Produto {produto['name']} adicionado à categoria Sobremesas")

for produto in entradas:
    Product.objects.create(category=categoria_entradas, **produto)
    print(f"Produto {produto['name']} adicionado à categoria Entradas")

print("Todos os produtos foram adicionados com sucesso!")
