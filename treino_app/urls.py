from django.urls import path
from . import views

urlpatterns = [
    path('fichas/', views.fichas_list, name='fichas_list'),
    path('fichas/nova/', views.criar_ficha, name='criar_ficha'),
]
