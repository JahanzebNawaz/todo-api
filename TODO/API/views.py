from rest_framework import viewsets, status
from rest_framework import permissions
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from rest_framework.response import Response
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

    def get_queryset(self):
        if self.request.user.is_staff:
            return Todo.objects.all()
        return Todo.objects.filter(user=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
    
    def perform_destroy(self, instance):
        instance.delete()
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(data=serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if  self.request.user.is_staff or self.request.user == instance.user:
            self.perform_destroy(instance)
            custom_error = {"details": "Deleted Successfully!"}
            return Response(custom_error, status=status.HTTP_204_NO_CONTENT)
        custom_error = {"details": "User does not match with record user"}
        return Response(custom_error, status=status.HTTP_401_UNAUTHORIZED)
    