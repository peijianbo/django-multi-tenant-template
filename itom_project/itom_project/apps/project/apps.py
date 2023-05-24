from django.apps import AppConfig


class ProjectConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'itom_project.apps.project'
    verbose_name = '项目管理'

    def ready(self):
        super().ready()
        from . import signals
