from django.urls import include, path
from rest_framework import routers
from .views import EditorViewSet

router = routers.DefaultRouter()
router.register(r'editor', EditorViewSet, basename="editor")

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include ('rest_framework.urls', namespace='rest_framework')),
]