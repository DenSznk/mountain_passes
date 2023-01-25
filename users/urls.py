from django.urls import path

from users.views import UserDetailAPI, RegisterUserAPIView

app_name = 'users'

urlpatterns = [
    path("get-details", UserDetailAPI.as_view()),
    path('register', RegisterUserAPIView.as_view()),
]
