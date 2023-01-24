from django.urls import path

from mountain_pass.views import UserDetailAPI, RegisterUserAPIView

urlpatterns = [
    path("get-details", UserDetailAPI.as_view()),
    path('register', RegisterUserAPIView.as_view()),
]
