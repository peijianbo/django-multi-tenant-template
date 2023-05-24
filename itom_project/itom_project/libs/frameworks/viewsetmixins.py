
from django.utils.translation import ugettext_lazy as _

from itom_project.libs.frameworks.errors import Error
from itom_project.libs.frameworks.exceptions import ItomException


class ItomViewSetMixin:
    """
    validate request body data. there will raise an Exception if validate failed.
    validate exist:
        validate_request(request, 'name', 'password')
    validate exist and type:
        validate_request(request, ('ids', List), ('file', File))
    validate exist and whether in given values:
        validate_request(request, ('type', ('delete', 'create')))
    """
    @classmethod
    def validate_request(cls, request, *args):
        request_data = []
        for key in args:
            if isinstance(key, tuple):
                key, type = key
                if key not in request.data:
                    raise ItomException(Error.REQUEST_DATA_MISSING, extra=key)

                flag = False
                try:
                    flag = isinstance(request.data[key], type)
                except:
                    flag = request.data[key] in type
                if not flag:
                    raise ItomException(Error.REQUEST_DATA_TYPE_ERROR, extra=_(f'`{key}`期望是{str(type)}类型'))
            else:
                if key not in request.data:
                    raise ItomException(Error.REQUEST_DATA_MISSING, extra=key)
            request_data.append(request.data[key])
        return request_data
