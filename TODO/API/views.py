from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from API.permissions.permissions import IsAdminOrOwner
from API.serialzers import TodoSerializer
from API.models import Todo

# Create your views here.

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated, IsAdminOrOwner,)
    
    filterset_fields = {
        "completed": ('exact',),
        "description": ('icontains',),
    }

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def get_queryset(self):
        if self.request.user.is_staff:
            return Todo.objects.all()
        return Todo.objects.filter(user=self.request.user)

    