from django.db import models
from django.utils.translation import ugettext_lazy as _
from itom_project.libs.frameworks.models import BaseModel


class Project(BaseModel):
    class Status(models.TextChoices):
        ONLINE = 'ONLINE', _('待上线')
        RUNNING = 'RUNNING', _('运行中')
        OFFLINE = 'OFFLINE', _('待下架')
        ARCHIVED = 'ARCHIVED', _('已归档')

    name = models.CharField(max_length=64, verbose_name=_('项目名称'))
    status = models.CharField(max_length=16, default=Status.ONLINE, choices=Status.choices, verbose_name=_('状态'))

    class Meta:
        db_table = 'itom_project'
        ordering = ['-create_time']
        verbose_name = _('项目')
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
