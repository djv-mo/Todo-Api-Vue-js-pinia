from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from .permissions import IsUser
from rest_framework.permissions import IsAuthenticated

class TaskViewSet(viewsets.ModelViewSet):

    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated, IsUser,)
    queryset = Task.objects.all()

    def get_queryset(self):
        return Task.objects.select_related('user').filter(user=self.request.user).order_by('-id')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
