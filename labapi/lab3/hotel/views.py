from rest_framework import viewsets
from hotel.serializers import hotelSerializer, roomSerializer, showSerializer
from hotel.models import hotel, show, room


class hotelViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать акции компаний
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = hotel.objects.all().order_by('stars')
    serializer_class = hotelSerializer  # Сериализатор для модели

class roomViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать акции компаний
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = room.objects.all().order_by('price')
    serializer_class = roomSerializer  # Сериализатор для модели

class showlViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать акции компаний
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = show.objects.all().order_by('full_name')
    serializer_class = showSerializer # Сериализатор для модели