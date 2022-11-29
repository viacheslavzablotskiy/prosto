from __future__ import absolute_import, unicode_literals
from celery import shared_task, Celery

from celery.schedules import crontab
from django.core.mail import EmailMessage


# celery = Celery('tasks', broker='pyamqp://guest@localhost//')
# import os
# os.environ['DJANGO_SETTING_MODULE'] = 'drfsite.setting'
@shared_task
def adding_task(x, y):
    return x + y
