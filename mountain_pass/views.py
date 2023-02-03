from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView, UpdateAPIView
from rest_framework.viewsets import ModelViewSet

from . import serializers
from .models import Area, Cords, MountainPass, Photo
from .serializers import (AreaSerializer, CordsSerializer,
                          MountainPassSerializer, MountainPassUpdateSerializer,
                          PhotoSerializer)


class AreaViewSet(ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer

    def perform_destroy(self, instance):
        if instance.has_inherited_object():
            raise ValidationError("Cannot delete object with inherited objects")
        instance.delete()


class MountainPassViewSet(ModelViewSet):
    queryset = MountainPass.objects.all().prefetch_related('user', 'area', 'cords')

    def get_serializer_class(self):
        if self.action == 'update' or self.action == 'partial_update':
            return serializers.MountainPassUpdateSerializer
        return serializers.MountainPassSerializer


class PhotoViewSet(ModelViewSet):
    queryset = Photo.objects.all().prefetch_related('mountain_pass')
    serializer_class = PhotoSerializer


class CordsViewSet(ModelViewSet):
    queryset = Cords.objects.all()
    serializer_class = CordsSerializer


class MountainPassUpdate(UpdateAPIView):
    queryset = MountainPass.objects.all().prefetch_related('user', 'area', 'cords')
    serializer_class = MountainPassUpdateSerializer


class MountainPassListView(ListAPIView):
    serializer_class = MountainPassSerializer

    def get_queryset(self):
        email = self.kwargs['email']
        return MountainPass.objects.filter(user__email=email)
