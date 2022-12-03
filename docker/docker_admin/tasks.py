from __future__ import absolute_import, unicode_literals

from time import sleep

from celery import shared_task, Celery

from celery.schedules import crontab
from django.contrib.auth.models import User
from django.core.mail import EmailMessage, send_mail


# app = Celery('tasks', backend='redis://127.0.0.1:6379', broker='redis://127.0.0.1:6379')
# app.conf.broker_url = 'redis://127.0.0.1:6379/0'

@shared_task
def adding_task(x, y):
    return x + y


@shared_task()
def send_feedback_email_task():

    sleep(5)
    # Simulate expensive operation(s) that freeze Django
    send_mail(
        subject="Your Feedback",
        message=f"Thank you!",
        from_email="zlava.mag@gmail.com",
        recipient_list=['zlava.mag@gmail.com'],
        fail_silently=False
    )
