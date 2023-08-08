from django.contrib import admin
from django.urls import include, path

from authusers.views import (alterar_papel, cadastro, deletar_usuario,
                             listar_usuarios, login)
from demoapp.views import adicionar_tarefa, listar_tarefas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cadastrar/', adicionar_tarefa, name='cadastrar'),
    path('listar/', listar_tarefas, name='listar'),
    path('login/', login, name='login'),
    path('cadastro/', cadastro, name='cadastro'),
    path('listarusers/', listar_usuarios, name='listar_usuarios'),
    path('usuarios/<str:matricula>/', deletar_usuario, name='deletar_usuario'),
    path('usuarios/<str:matricula>/alterar-papel/', alterar_papel, name='alterar_papel'),
]
