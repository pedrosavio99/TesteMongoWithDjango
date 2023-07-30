from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Todo
from .serializers import TodoSerializer


@api_view(['POST'])
def adicionar_tarefa(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def listar_tarefas(request):
    tarefas = Todo.objects.all()
    serializer = TodoSerializer(tarefas, many=True)
    return Response(serializer.data)
