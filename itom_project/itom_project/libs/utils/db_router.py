from itom_project.libs.frameworks.exceptions import DBRouterException
from itom_project.libs.utils.tenant_util import TenantUtil


class DBRouter:
    def db_for_read(self, model, **hints):
        tenant_id = TenantUtil.get_current_tenant()
        if not tenant_id:
            # raise DBRouterException('DBRouter get `tenant_id` failed')
            return 'default'
        return tenant_id

    def db_for_write(self, model, **hints):
        tenant_id = TenantUtil.get_current_tenant()
        if not tenant_id:
            # raise DBRouterException('DBRouter get `tenant_id` failed')
            return 'default'
        return tenant_id

    def allow_relation(self, obj1, obj2, **hints):
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return True
