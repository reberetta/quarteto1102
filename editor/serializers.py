from rest_framework import serializers
from .models import Editor


class EditorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editor
        fields = '__all__'