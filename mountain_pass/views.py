from rest_framework.generics import UpdateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import (MountainPass, Area, Cords, Photo, )
from .serializers import (AreaSerializer,
                          MountainPassSerializer, CordsSerializer, PhotoSerializer
                          )


class AreaViewSet(ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer
    permission_classes = [IsAuthenticated]


class MountainPassViewSet(ModelViewSet):
    queryset = MountainPass.objects.all().prefetch_related('user', 'area', 'cords')
    serializer_class = MountainPassSerializer
    permission_classes = [IsAuthenticated]


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
    serializer_class = MountainPassSerializer
    permission_classes = [IsAuthenticated]


class MountainPassListView(ListAPIView):
    serializer_class = MountainPassSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self, ):
        queryset = P

        return queryset
