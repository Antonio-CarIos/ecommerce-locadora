from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('detalhe/<int:id>', views.detalhes, name='detalhe'),
    path('registrar/', views.registrar_usuario, name='registrar'),
    path('logar/', views.login_usuario, name='logar'),
    path('logout/', views.logout_usuario, name='logout_usuario'),

    path('dashboard/', views.dashboards, name='dashboard'),
    path('cadastro/', views.cadastrar_dvd, name='cadastrar'),
    path('editar/<int:id>', views.editado, name='editar'),
    path('deletar/<int:id>', views.deletado, name='excluir'),

    path('catalogo/', views.lista_produtos, name='catalogo'),
    path('carrinho/', views.carrinho, name='carrinho'),
    path('adicionar-carrinho/<int:id>', views.adicionar_ao_carrinho, name='adicionar_carrinho'),
    path('remover-carrinho/<int:item_id>', views.remover_item_carrinho, name='remover_carrinho'),
    path('sobre/', views.sobre, name='sobre'),
]


