import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery_rabbitmq_random_user.settings')
app = Celery('django_celery_rabbitmq_random_user')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()