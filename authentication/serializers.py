from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'password', 'full_name', 'is_active', 'is_staff', 'is_superuser', 'date_joined', 'last_login')
        extra_kwargs = {
            'password': {'write_only': True},
            'is_active': {'read_only': True},
            'is_staff': {'read_only': True},
            'is_superuser': {'read_only': True},
            'date_joined': {'read_only': True},
            'last_login': {'read_only': True},
        }
        read_only_fields = ('is_active', 'is_staff', 'is_superuser', 'date_joined', 'last_login')
        write_only_fields = ('password',)

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user
    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.full_name = validated_data.get('full_name', instance.full_name)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.is_staff = validated_data.get('is_staff', instance.is_staff)
        instance.is_superuser = validated_data.get('is_superuser', instance.is_superuser)
        instance.save()
        return instance
    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long.")
        return value
    def validate_email(self, value):
        if not value:
            raise serializers.ValidationError("Email is required.")
        return value
    def validate_full_name(self, value):
        if not value:
            raise serializers.ValidationError("Full name is required.")
        return value
    def validate(self, data):
        if not data.get('email'):
            raise serializers.ValidationError("Email is required.")
        if not data.get('full_name'):
            raise serializers.ValidationError("Full name is required.")
        return data
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['id'] = instance.id
        representation['email'] = instance.email
        representation['full_name'] = instance.full_name
        representation['is_active'] = instance.is_active
        representation['is_staff'] = instance.is_staff
        representation['is_superuser'] = instance.is_superuser
        representation['date_joined'] = instance.date_joined
        representation['last_login'] = instance.last_login
        return representation