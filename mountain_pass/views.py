from rest_framework.generics import UpdateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
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
    permission_classes = [IsAuthenticated]


class MountainPassViewSet(ModelViewSet):
    queryset = MountainPass.objects.all().prefetch_related('user', 'area', 'cords')
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'update' or self.action == 'partial_update':
            return serializers.MountainPassUpdateSerializer
        return serializers.MountainPassSerializer


class PhotoViewSet(ModelViewSet):
    queryset = Photo.objects.all().prefetch_related('mountain_pass')
    serializer_class = PhotoSerializer
    permission_classes = [IsAuthenticated]


class CordsViewSet(ModelViewSet):
    queryset = Cords.objects.all()
    serializer_class = CordsSerializer
    permission_classes = [IsAuthenticated]


class MountainPassUpdate(UpdateAPIView):
    queryset = MountainPass.objects.all().prefetch_related('user', 'area', 'cords')
    serializer_class = MountainPassUpdateSerializer
    permission_classes = [IsAuthenticated]


class MountainPassListView(ListAPIView):
    serializer_class = MountainPassSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        email = self.kwargs['email']
        return MountainPass.objects.filter(user__email=email)
