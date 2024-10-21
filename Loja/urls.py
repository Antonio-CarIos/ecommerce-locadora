from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('detalhe/<int:id>', views.detalhes, name='detalhe'),
    path('registrar/', views.registrar_usuario, name='registrar'),
    path('dashboard/', views.dashboards, name='dashboard'),
    path('cadastro/', views.cadastrar_dvd, name='cadastrar'),
    path('editar/<int:id>', views.editado, name='editar'),
    path('deletar/<int:id>', views.deletado, name='excluir'),
]


