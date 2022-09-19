from django.urls import path

from django_redis.register.views import RegisterView, HashRegisterView, HashRegisterDetailView

app_name = 'register'

urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('register/hash', HashRegisterView.as_view(), name='register-hash'),
    path('register/<str:id>', HashRegisterDetailView.as_view(), name='register-hash-detail'),
]
