"""demoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from authusers.views import cadastro, listar_usuarios, login
from demoapp.views import adicionar_tarefa, listar_tarefas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cadastrar/', adicionar_tarefa, name='cadastrar'),
    path('listar/', listar_tarefas, name='listar'),
    path('login/', login, name='login'),
    path('cadastro/', cadastro, name='cadastro'),
    path('listarusers/', listar_usuarios, name='listar_usuarios'),
    # path('demoapp/', include('demoapp.urls')), # Adiciona as URLs do app demoapp
]
