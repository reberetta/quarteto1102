from rest_framework import viewsets
from .serializers import EditorSerializer
from .models import Editor

class EditorViewSet(viewsets.ModelViewSet):
    queryset = Editor.objects.all().order_by('name')
    serializer_class = EditorSerializer
