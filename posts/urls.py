from django.urls import path
from . import views
from .views import PostListView

urlpatterns = [    
    path('lista/', views.lista_posts, name='lista_posts'),
    path('cbv-lista/', PostListView.as_view(), name='cbv_lista_posts'),
]