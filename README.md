# Sistema de Gerenciamento de Restaurante API

API para gerenciamento de mesas, categorias, produtos, adicionais e pedidos de restaurante.

## Tecnologias

- Django 5.2
- Django REST Framework 3.16.0
- Django Filter 24.1
- DRF YASG 1.21.10
- JWT Authentication

## Documentação da API

A documentação completa da API está disponível em:

- `/swagger/` - Interface Swagger
- `/redoc/` - Interface ReDoc

## Endpoints Principais

### Autenticação

- `POST /token/` - Obter token JWT
- `POST /token/refresh/` - Renovar token JWT

### Mesas

- `GET /tables/` - Listar todas as mesas
- `POST /tables/` - Criar nova mesa
- `POST /tables/{table_id}/set-unavailable/` - Marcar mesa como indisponível
- `POST /tables/{table_id}/set-available/` - Marcar mesa como disponível

#### Exemplo de criação de mesa

```json
POST /tables/
{
  "table_number": "10",
  "capacity": 4
}
```

#### Exemplo de marcação de mesa como indisponível

```json
POST /tables/1/set-unavailable/
{
  "seats": 3
}
```

### Produtos

- `GET /products/` - Listar todos os produtos
- `POST /products/` - Criar novo produto
- `GET /products/{product_id}/` - Detalhes de um produto
- `PUT /products/{product_id}/` - Atualizar produto
- `DELETE /products/{product_id}/` - Excluir produto

#### Filtros disponíveis para produtos

- `GET /products/?category=1` - Filtrar produtos por categoria
- `GET /products/?is_available=true` - Filtrar produtos por disponibilidade
- `GET /products/?search=pizza` - Buscar produtos por nome

#### Exemplo de resposta da listagem de produtos

```json
[
  {
    "id": 1,
    "name": "Pizza Margherita",
    "description": "Pizza tradicional italiana",
    "price": 45.90,
    "category": 1,
    "is_available": true
  },
  {
    "id": 2,
    "name": "Hambúrguer Clássico",
    "description": "Hambúrguer com queijo e salada",
    "price": 32.50,
    "category": 2,
    "is_available": true
  }
]
```

### Pedidos

- `GET /orders/` - Listar todos os pedidos
- `POST /orders/` - Criar novo pedido
- `GET /orders/{order_id}/` - Detalhes de um pedido
- `PATCH /orders/{order_id}/status/` - Atualizar status do pedido
- `GET /tables/{table_id}/orders/` - Listar pedidos de uma mesa

#### Exemplo de criação de pedido

```json
POST /orders/
{
  "table": 1,
  "items": [
    {
      "product": 1,
      "quantity": 2,
      "notes": "Sem cebola",
      "additionals": [
        {
          "additional": 3,
          "quantity": 1
        }
      ]
    },
    {
      "product": 5,
      "quantity": 1,
      "notes": "",
      "additionals": []
    }
  ]
}
```

#### Exemplo de atualização de status do pedido

```json
PATCH /orders/1/status/
{
  "status": "finalizado"
}
```

### Categorias

- `GET /categories/` - Listar todas as categorias
- `POST /categories/` - Criar nova categoria

### Adicionais

- `GET /additionals/` - Listar todos os adicionais
- `POST /additionals/` - Criar novo adicional

## Sistema de Sessões para Mesas

O sistema implementa um controle de sessões para mesas, permitindo que a mesma mesa seja usada várias vezes ao longo do dia sem misturar os pedidos de diferentes clientes.

- Cada mesa possui um contador `current_session` que é incrementado quando a mesa é marcada como disponível
- Cada pedido é associado à sessão atual da mesa no momento de sua criação
- Ao listar os pedidos de uma mesa, apenas os pedidos da sessão atual são exibidos
- Isso garante que pedidos de clientes anteriores não apareçam para novos clientes na mesma mesa

## Configuração do Projeto

1. Clone o repositório
2. Instale as dependências: `pip install -r requirements.txt`
3. Execute as migrações: `python manage.py migrate`
4. Crie um superusuário: `python manage.py createsuperuser`
5. Inicie o servidor: `python manage.py runserver`
