from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_heroes, name='hello_heroes'),
]
