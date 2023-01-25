from rest_framework.generics import UpdateAPIView, ListAPIView
from rest_framework.viewsets import ModelViewSet

from .models import (MountainPass, Photo,
                     Cords, User, Area,
                     )
from .serializers import (MountainPassSerializer, PhotoSerializer,
                          CordsSerializer, MountainPassUpdateSerializer,
                          )

