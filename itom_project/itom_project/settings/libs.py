"""
extra packages settings
"""
import os


# Celery
CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL', 'redis://127.0.0.1:6379/0')
CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND', 'django-db')


# Account micro
ACCOUNT_MICRO_HOST = os.getenv('ACCOUNT_MICRO_HOST', 'http://192.168.10.21:8100')
ACCOUNT_MICRO_LIST_ORG_PATH = os.getenv('ACCOUNT_MICRO_LIST_ORG_PATH', 'api.account.service.v1.Account/GetOrgTree?depth=0')
ACCOUNT_MICRO_RETRIEVE_ORG_PATH = os.getenv('ACCOUNT_MICRO_RETRIEVE_ORG_PATH', 'api.account.service.v1.Account/GetDepartment')
ACCOUNT_MICRO_RETRIEVE_PATH_ORG_PATH = os.getenv('ACCOUNT_MICRO_RETRIEVE_PATH_ORG_PATH', 'api.account.service.v1.Account/GetDepartmentsByIDs')

# CMDB micro
CMDB_MICRO_HOST = os.getenv('CMDB_MICRO_HOST', 'http://127.0.0.1:6789')
CMDB_MICRO_DEL_PROJECT_CONFIRM_PATH = os.getenv('CMDB_MICRO_DEL_PROJECT_CONFIRM_PATH', 'api.account.service.v1.Account/GetOrgTree')
