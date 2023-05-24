import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _


class BaseModel(models.Model):

    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    create_by = models.CharField(max_length=32, null=True, blank=True, verbose_name=_('创建者'), help_text=_('创建者'))
    update_by = models.CharField(max_length=32, null=True, blank=True, verbose_name=_('修改者'), help_text=_('修改者'))
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=_('创建时间'))
    update_time = models.DateTimeField(auto_now=True, verbose_name=_('更新时间'))

    class Meta:
        abstract = True
