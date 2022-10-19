from hotel.models import hotel, show, room
from rest_framework import serializers


class hotelSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = hotel
        # Поля, которые мы сериализуем
        fields = ["id", "name", "address", "stars", "country", 'image']

class roomSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = room
        # Поля, которые мы сериализуем
        fields = ["id", "category", "max_count", "bed_type", "price", 'total', 'hotel_id_id']

class showSerializer(serializers.ModelSerializer):
    class Meta:
            # Модель, которую мы сериализуем
            model = show
            # Поля, которые мы сериализуем
            fields = ["id", "full_name"]