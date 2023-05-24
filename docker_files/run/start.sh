#!/bin/bash
# 启动服务
python manage.py collectstatic --noinput
python manage.py makemigrations --noinput
python manage.py migrate --database all

if [ "$ENABLE_CELERY" == 'true' ]
then
  celery worker -A itom_project.celery_app -l info --logfile='logs/celery_worker.log' &
  celery beat -A itom_cmdb.celery_app -l info --logfile='logs/celery_beat.log' --pidfile= &
fi

uwsgi --ini /data/server/run/uwsgi.ini

