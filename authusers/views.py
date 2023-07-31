import json

from django.http import JsonResponse
# Create your views here.
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt

from .models import User


@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        matricula = data.get('matricula')
        senha = data.get('senha')
        user = get_object_or_404(User, matricula=matricula, senha=senha)
        return JsonResponse({'message': 'Login realizado com sucesso!', 'matricula': user.matricula})
    return JsonResponse({'message': 'Método inválido! Use POST para login.'}, status=400)

@csrf_exempt
def cadastro(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        matricula = data.get('matricula')
        senha = data.get('senha')
        if len(matricula) == 4 and len(senha) == 4:
            user, created = User.objects.get_or_create(matricula=matricula, senha=senha)
            if created:
                return JsonResponse({'message': 'Cadastro realizado com sucesso!', 'matricula': user.matricula})
            else:
                return JsonResponse({'message': 'Usuário já cadastrado!'}, status=400)
        else:
            return JsonResponse({'message': 'Matrícula e senha devem ter 4 dígitos!'}, status=400)
    return JsonResponse({'message': 'Método inválido! Use POST para cadastro.'}, status=400)

def listar_usuarios(request):
    users = User.objects.all()
    data = [{'matricula': user.matricula} for user in users]
    return JsonResponse(data, safe=False)
