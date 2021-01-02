from celery import Celery
from .celeryconfig import config as celery_config
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_scheduler.settings')

app = Celery('tasks')
app.config_from_object(celery_config)
app.autodiscover_tasks()
