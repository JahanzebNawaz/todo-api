from rest_framework import serializers

from API.models import Todo


class TodoSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Todo
        fields = '__all__'


