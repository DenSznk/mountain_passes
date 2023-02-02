from rest_framework import status
from rest_framework.exceptions import ValidationError, NotFound
from rest_framework.generics import UpdateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from . import serializers
from .models import (MountainPass, Area, Cords, Photo, )
from .serializers import (AreaSerializer, CordsSerializer,
                          MountainPassSerializer,
                          MountainPassUpdateSerializer, PhotoSerializer
                          )


class AreaViewSet(ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer


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
