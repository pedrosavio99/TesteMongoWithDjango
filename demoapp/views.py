from rest_framework.decorators import api_view
from rest_framework.response import Response

from authusers.models import User
from demoapp.models import Todo

from .serializers import TaskSerializer


@api_view(['DELETE'])
def deletar_tarefa(request, tarefa_id):
    try:
        tarefa = Todo.objects.get(pk=tarefa_id)
    except Todo.DoesNotExist:
        return Response({'message': 'Tarefa não encontrada.'},status=404)

    tarefa.delete()
    return Response({'message': 'Tarefa deletada com sucesso.'}, status=200)


@api_view(['POST'])
def adicionar_tarefa(request):
    title = request.data["title"]
    description = request.data["description"]
    assignee_matricula = request.data["assigner"] 
    assignees = request.data["assignees"]  
    created_at = request.data["created_at"]  
    updated_at = request.data["updated_at"]  

    try:
        assigner = User.objects.get(matricula=assignee_matricula, role='adm')  # Filtrar pelo papel de 'adm'
    except User.DoesNotExist:
        return Response({'message': 'Usuário atribuidor não encontrado ou não é um administrador.'}, status=400)

    serializer = TaskSerializer(data={
        'title': title,
        'description': description,
        'assigner': assigner.name, 
        'assignees': assignees,
        "created_at": created_at, 
        "updated_at": updated_at
    })

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def listar_tarefas(request):
    tarefas = Todo.objects.all()
    serializer = TaskSerializer(tarefas, many=True)
    return Response(serializer.data)
