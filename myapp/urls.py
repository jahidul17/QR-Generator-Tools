from django.urls import path
from . import views

urlpatterns = [
    path('qr/', views.generator, name='generator'),
]
