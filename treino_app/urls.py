from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('perfil/', views.perfil_usuario, name='perfil'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
    path('fichas/', views.fichas_list, name='fichas_list'),
    path('fichas/nova/', views.criar_ficha, name='criar_ficha'),
    path('fichas/<int:ficha_id>/adicionar-item/', views.adicionar_item_ficha, name='adicionar_item_ficha'),
    path('itens/<int:item_id>/editar/', views.editar_item_ficha, name='editar_item_ficha'),
    path('itens/<int:item_id>/excluir/', views.excluir_item_ficha, name='excluir_item_ficha'),
    path('fichas/<int:ficha_id>/', views.ficha_detalhe, name='ficha_detalhe'),
    path('signup/', views.signup_view, name='signup'),  # nova rota de cadastro [web:407][web:422]
]
