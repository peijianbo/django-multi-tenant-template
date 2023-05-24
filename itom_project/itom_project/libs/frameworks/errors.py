from django.utils.translation import ugettext_lazy as _


class Code:
    """与前端协商的自定义错误码"""

    # 通用错误码
    # 2000表示msg格式为字符串，前端可以直接展示{'msg':String, code:2000}
    C_2000 = 2000

    # ValidationError错误码
    # 2110表示msg格式为dict，前端需要解析展示{'msg':Dict, code:2110}
    C_2110 = 2110
    # 2120表示sg格式为List，前端需要解析展示{'msg':List, code:2120}
    C_2120 = 2120

class Error:
    SUCCESS = (200, _("OK"))
    UNKNOWN = (500, _("未知错误"))

    # Common
    DELETE_FAILED = (400, _("删除失败"))
    ARCHIVE_FAILED = (400, _("归档失败"))
    REMOTE_CONNECTION_ERROR = (503, _('远程访问错误'))

    # Request
    REQUEST_DATA_MISSING = (400, u"请求数据缺失")
    REQUEST_DATA_TYPE_ERROR = (400, _('请求体数据类型错误'))

    # File
    FILE_NOT_EXIST = (404, _("文件不存在"))
    FILE_TYPE_ERROR = (400, _("文件类型错误"))

    # Authentication
    TENANT_ID_NOT_FOUND = (400, _('租户ID获取失败'))
    ADMIN_USERNAME_FORMAT_ERROR = (401, _('用户名格式错误'))
    AUTHENTICATION_FIELD = (401, _('认证失败'))

    # Yunion
    YUNION_CLIENT_ERROR = (400, _("云联壹云客户端错误"))
