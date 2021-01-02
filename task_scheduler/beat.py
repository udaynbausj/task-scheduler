from celery.schedules import crontab

config = {
    'ping-every-minute': {
        'task': 'ping.tasks.status_check',
        'schedule': crontab(hour='*', minute="*")
    }
}
