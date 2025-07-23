from django.urls import path
from . import views
from .views import HeroListView

urlpatterns = [    
    path('lista/', views.lista_herois, name='lista_herois'),
    path('cbv-lista/', HeroListView.as_view(), name='cbv_lista_herois'),
]