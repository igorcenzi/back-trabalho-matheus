from rest_framework import serializers
from tables.models import HallTables

class HallTablesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HallTables
        fields = '__all__'
        read_only_fields = ('id', 'seats')