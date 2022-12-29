from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(
        viewsets.GenericViewSet):
    """
    Updates and retrieves user accounts
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
