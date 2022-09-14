from django.urls import path

from django_redis.register.views import RegisterView

app_name = 'register'

urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
]
