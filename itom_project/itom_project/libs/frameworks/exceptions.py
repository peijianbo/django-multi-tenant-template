from django.http import JsonResponse

from itom_project.libs.frameworks.errors import Error, Code


class ItomResponse(object):
    def __init__(self, status=Error.SUCCESS, msg=None, extra=None, code=Code.C_2000, **kwargs):
        self.status_code, default_msg = status
        msg = msg or default_msg
        if extra is not None:
            msg = "%s (%s)" % (msg, extra)
        self.data = kwargs
        self.data.update({'msg': msg, 'code': code})

    def __str__(self):
        return str(self.data)

    def build_response(self):
        return JsonResponse(self.data, status=self.status_code)


class ItomException(ItomResponse, Exception):
    pass


class WarningException(ItomResponse, Exception):
    pass


class DBRouterException(Exception):
    pass
