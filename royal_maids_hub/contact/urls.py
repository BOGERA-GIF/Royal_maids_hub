from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('application/', views.application, name='application'),
    path('success/', views.success, name='success'),
    path('about/', views.about_view, name='about_view'),
    path('booking/', views.booking, name='booking'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    
]
