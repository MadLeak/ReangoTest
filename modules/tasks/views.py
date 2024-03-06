"""
Task views
"""

from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer


# Create your views here.
class TaskView(viewsets.ModelViewSet):
    """
    Task view set
    """

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
