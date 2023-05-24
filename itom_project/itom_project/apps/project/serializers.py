
from itom_project.libs.frameworks.serializers import DisplayModelSerializer, ModifierModelSerializer
from .models import Project


class ProjectSerializer(ModifierModelSerializer,
                        DisplayModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'
