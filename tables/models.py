from django.db import models

# Create your models here.
class HallTables(models.Model):
    id = models.BigAutoField(primary_key=True)
    table_number = models.CharField(max_length=10, unique=True)
    seats = models.IntegerField()  # This will be used to store the current number of people when table is occupied
    capacity = models.IntegerField(default=0)  # This will store the original capacity of the table
    is_available = models.BooleanField(default=True)
    current_session = models.IntegerField(default=0)  # Contador de sessões para rastrear pedidos

    def __str__(self):
        return f"Table {self.table_number} - Seats: {self.seats} - Available: {self.is_available}"