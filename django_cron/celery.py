# myproject/celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_cron.settings')

app = Celery('django_cron')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.update(
    broker_url='redis://localhost:6379',
    result_backend='redis://localhost:6379',
)

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
