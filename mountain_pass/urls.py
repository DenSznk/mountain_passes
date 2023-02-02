from django.urls import path, include
from rest_framework import routers

from mountain_pass.views import (AreaViewSet, MountainPassViewSet,
                                 PhotoViewSet, CordsViewSet, MountainPassListView,
                                 )

app_name = 'mountain_pass'

router = routers.DefaultRouter()
router.register('area', AreaViewSet)
router.register('photo', PhotoViewSet)
router.register('mountain-pass', MountainPassViewSet)
router.register('cords', CordsViewSet)

urlpatterns = [
    path('mountain-pass-list/<email>/', MountainPassListView.as_view()),
]
urlpatterns += router.urls
