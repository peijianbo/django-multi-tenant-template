import json

from django.conf import settings
from django.utils.deprecation import MiddlewareMixin
from django.utils.functional import SimpleLazyObject
from django.utils.translation import ugettext_lazy as _

from itom_project import thread_local
from itom_project.libs.frameworks.errors import Error
from itom_project.libs.frameworks.exceptions import ItomResponse
from itom_project.libs.utils.common_util import chain_getattr
from itom_project.libs.utils.tenant_util import TenantUtil

import logging
logger = logging.getLogger('django')


# class AuthenticationMiddleWare(MiddlewareMixin):
#     @classmethod
#     def token_authenticate(cls, request):
#         token = request.headers.get('x-md-global-token')
#         if token:
#             try:
#                 user_info = decode_token(token)
#             except:
#                 logger.info(_(f'token解析失败({token})'))
#                 return None
#             user_info.update({'username': user_info['dispname'], 'id': user_info['account_id']})
#             user = SimpleLazyObject(lambda: UserInfo.get_user(**user_info))
#             return user
#         return None
#
#     @classmethod
#     def basic_authenticate(cls, request):
#         user_info = eval(str(request.META.get('HTTP_USER_INFO', '{}')))
#         if user_info:
#             user = SimpleLazyObject(lambda: UserInfo.get_user(**user_info))
#             return user
#         return None
#
#     def process_request(self, request):
#         user = self.basic_authenticate(request)
#         if user:
#             request.user_ = user
#             return None
#         user = self.token_authenticate(request)
#         if not user:
#             return ItomResponse(status=Error.AUTHENTICATION_FIELD).build_response()
#         request.user_ = user
#         return None


class CacheTenantMiddleWare(MiddlewareMixin):
    def process_request(self, request):
        tenant_id = chain_getattr(request, 'user_', 'tenant_id')
        if request.path.startswith(('/docs', f'/{settings.ADMIN_PREFIX}')):
            if not tenant_id:
                return None
        if not tenant_id:
            return ItomResponse(status=Error.TENANT_ID_NOT_FOUND).build_response()
        TenantUtil.set_current_tenant(tenant_id)
        return None

    def process_response(self, request, response):
        thread_local.__release_local__()
        return response


class DjangoAdminSupportMiddleWare(MiddlewareMixin):
    admin_user_info = {'tenant_id': ''}

    @classmethod
    def handle_admin_userinfo(cls, request):
        if request.path.startswith(f'/{settings.ADMIN_PREFIX}/login') and request.method == 'POST':
            username, tenant_id = request.POST.get('username', '@').split('@')
        else:
            user_info = json.loads(request.COOKIES.get('user_info', '{}'))
            tenant_id = user_info.get('tenant_id', '')
        admin_user_info = cls.admin_user_info.copy()
        admin_user_info.update({'tenant_id': tenant_id})
        return admin_user_info

    def process_request(self, request):
        if request.path.startswith(f'/{settings.ADMIN_PREFIX}'):
            admin_user_info = self.handle_admin_userinfo(request)
            TenantUtil.set_current_tenant(admin_user_info['tenant_id'])
            request.META['HTTP_USER_INFO'] = admin_user_info
        return None

    def process_response(self, request, response):
        if request.path.startswith(f'/{settings.ADMIN_PREFIX}'):
            admin_user_info = request.META['HTTP_USER_INFO']
            TenantUtil.set_current_tenant(admin_user_info['tenant_id'])
            response.set_cookie('user_info', json.dumps(admin_user_info))
        return response
