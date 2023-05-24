from itom_project import thread_local

TENANT_KEY = 'current_tenant_id'


class TenantUtil:
    @classmethod
    def set_current_tenant(cls, tenant_id):
        setattr(thread_local, TENANT_KEY, tenant_id)

    @classmethod
    def get_current_tenant(cls):
        return getattr(thread_local, TENANT_KEY, None)

    @classmethod
    def release_current_tenant(cls):
        thread_local.__delattr__(TENANT_KEY)
