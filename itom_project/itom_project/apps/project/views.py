from rest_framework.viewsets import ModelViewSet

from .models import Project
from .serializers import ProjectSerializer


class ProjectViewSet(ModelViewSet):
    ordering_fields = ('name', )
    filter_fields = ('id', 'name',)
    search_fields = filter_fields

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
