from rest_framework import routers
from django.urls import path, include
from mountain_pass.views import (AreaViewSet, MountainPassViewSet,
                                 PhotoViewSet, CordsViewSet, MountainPassUpdate, MountainPassListView,
                                 )
app_name = 'mountain_pass'


router = routers.DefaultRouter()
router.register('area', AreaViewSet)
router.register('photo', PhotoViewSet)
router.register('mountain-pass', MountainPassViewSet)
router.register('cords', CordsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('mountain-pass-list/<int:pk>', include(router.urls)),
]