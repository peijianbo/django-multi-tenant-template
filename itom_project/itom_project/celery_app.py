# -*- coding: utf-8 -*-
import os

from celery.schedules import crontab
from django.conf import settings

from kombu import Queue, Exchange
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'itom_project.settings.settings')

app = Celery('celery', broker=settings.CELERY_BROKER_URL, backend=settings.CELERY_RESULT_BACKEND)
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.update(
    # enable CELERY_ALWAYS_EAGER=True can debug you task
    CELERY_ALWAYS_EAGER=True,
    CELERY_TASK_RESULT_EXPIRES=3600,
    CELERY_TASK_SERIALIZER='json',
    CELERY_ACCEPT_CONTENT=['json'],
    CELERY_RESULT_SERIALIZER='json',


    CELERYD_CONCURRENCY=20,
    CELERYD_FORCE_EXECV=True,
    CELERYD_MAX_TASKS_PER_CHILD=100,

    CELERY_DEFAULT_QUEUE='default',
    CELERY_DEFAULT_ROUTING_KEY='default',
    CELERY_QUEUES=(
        Queue('default', Exchange('default'), routing_key='default'),
        Queue('demo_queue', Exchange('demo_queue'), routing_key='demo_queue'),
    ),
    CELERY_TIMEZONE=settings.TIME_ZONE,
    CELERYBEAT_SCHEDULE={
        # # schedule1：execute task every five minutes(sync_host)
        # 'sync_host': {
        #     "task": "itom_project.apps.host.tasks.sync_host",
        #     "schedule": crontab(hour='*/5'),
        #     "args": (),
        # },
        # # schedule2：execute task every day at 2:00 a.m(sync_host)
        # 'sync_host': {
        #     "task": "itom_project.apps.host.tasks.sync_host",
        #     'schedule': crontab(minute=0, hour=2),
        #     "args": ()
        # },
        # # schedule3：execute task every month at 1st 6:00 a.m(sync_host)
        # 'sync_host': {
        #         "task": "itom_project.apps.host.tasks.sync_host",
        #         'schedule': crontab(hour=6, minute=0, day_of_month='1'),
        #         "args": ()
        # },
    }
)
