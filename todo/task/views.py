from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from .permissions import IsUser
from rest_framework.permissions import IsAuthenticated

class TaskViewSet(viewsets.ModelViewSet):

    queryset = Task.objects.order_by('-id')
    serializer_class = TaskSerializer
    # permission_classes = (IsAuthenticated, IsUser,)
