from django.db import models
class HallTables(models.Model):
    id = models.BigAutoField(primary_key=True)
    table_number = models.CharField(max_length=10, unique=True)
    seats = models.IntegerField()
    capacity = models.IntegerField(default=0)
    is_available = models.BooleanField(default=True)
    current_session = models.IntegerField(default=0)

    def __str__(self):
        return f"Table {self.table_number} - Seats: {self.seats} - Available: {self.is_available}"