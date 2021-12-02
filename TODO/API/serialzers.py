from rest_framework import serializers

from API.models import Todo


class TodoSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Todo
        fields = ['id', 'user', 'description', 'completed']



    def create(self, validated_data):
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        print(validated_data)
        return super().update(instance, validated_data)