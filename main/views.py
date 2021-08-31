from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from .models import TodoModel
from .serializers import ListTodoSerializer
# Create your views here.


class ListTodoView(ListAPIView):
    serializer_class = ListTodoSerializer
    queryset = TodoModel.objects.all()


class CreateTodoView(CreateAPIView):
    serializer_class = ListTodoSerializer


@api_view(['GET'])
def test_view(request):
    return Response({'success': True})
