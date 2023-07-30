from django.urls import path

from . import views

urlpatterns = [
    path('adicionar/', views.adicionar_tarefa, name='adicionar_tarefa'),
    path('listar/', views.listar_tarefas, name='listar_tarefas'),
]