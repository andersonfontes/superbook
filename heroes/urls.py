from django.urls import path
from . import views

urlpatterns = [    
    path('lista/', views.lista_herois, name='lista_herois'),
]