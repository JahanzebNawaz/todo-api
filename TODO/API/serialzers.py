from rest_framework_json_api import serializers

from API.models import Todo, Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"



class TodoSerializer(serializers.ModelSerializer):

    included_serializers = {
        'author': AuthorSerializer,
    }

    class Meta:
        model = Todo
        fields = "__all__"

