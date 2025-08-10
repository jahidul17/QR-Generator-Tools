from django.urls import path
from . import views

urlpatterns = [
    path('qr/', views.generator, name='generator'),
    path('about/',views.about, name='about'),
    path('contact/',views.contact, name='contact'),
]
