from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.db import DatabaseError, IntegrityError
from django.db.models import ProtectedError
from django.http import Http404
from django.utils.translation import ugettext_lazy as _

from rest_framework import status, exceptions
from rest_framework.response import Response
from rest_framework.views import set_rollback

from itom_project.libs.frameworks.errors import Code
from itom_project.libs.frameworks.exceptions import ItomException, WarningException

import logging
logger = logging.getLogger('django')


def exception_handler(exc, context):
    if isinstance(exc, Http404):
        exc = exceptions.NotFound()
    elif isinstance(exc, PermissionDenied):
        exc = exceptions.PermissionDenied()

    if isinstance(exc, exceptions.APIException):
        headers = {}
        if getattr(exc, 'auth_header', None):
            headers['WWW-Authenticate'] = exc.auth_header
        if getattr(exc, 'wait', None):
            headers['Retry-After'] = '%d' % exc.wait

        code = '-'
        if isinstance(exc, exceptions.ValidationError):
            code = Code.C_2110 if isinstance(exc.detail, dict) else Code.C_2120
        data = {'msg': exc.detail, 'code': code}

        set_rollback()
        return Response(data, status=exc.status_code, headers=headers)

    if isinstance(exc, ItomException):
        logger.error(exc)
        set_rollback()
        return Response(exc.data, status=exc.status_code)
    elif isinstance(exc, WarningException):
        logger.warning(exc)
        set_rollback()
        return Response(exc.data, status=exc.status_code)
    elif isinstance(exc, (DatabaseError, IntegrityError)):
        msg = _('数据库操作错误')
        if isinstance(exc, ProtectedError):
            objects_repr = [f'{obj._meta.verbose_name}:{obj.__str__()}' for obj in exc.protected_objects]
            msg = _(f'请先删除关联对象:{objects_repr}')
        data = {'msg': msg}
        logger.error(exc)
        set_rollback()
        return Response(data, status=status.HTTP_400_BAD_REQUEST)
    # Note: Unhandled exceptions will raise a 500 error.
    return None
