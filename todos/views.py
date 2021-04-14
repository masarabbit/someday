from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .serializers.common import TodoSerializer
from .models import Todo

class TodoListView(APIView):

  permission_classes = (IsAuthenticated, )
  
  #make todo
  def post(self, request):
      todo_to_create = TodoSerializer(data=request.data)
      if todo_to_create.is_valid():
          todo_to_create.save()
          return Response(todo_to_create.data, status=status.HTTP_201_CREATED)
      return Response(todo_to_create.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY) 
      

class TodoDetailView(APIView):

    permission_classes = (IsAuthenticated, )
    
    #delete todo
    def delete(self, request, pk):
        try:
            todo_to_delete = todo.objects.get(pk=pk)

            if todo_to_delete.owner.id != request.user.id: 
                raise PermissionDenied
              
            todo_to_delete.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Todo.DoesNotExist:
            raise NotFound()      