from rest_framework import viewsets
from .models import Todolist
from .serializers import Todoserielizers

# Create your views here.

class TodoAPI(viewsets.ModelViewSet):
    queryset = Todolist.objects.all()
    serializer_class =Todoserielizers