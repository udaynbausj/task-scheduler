from task_scheduler.celery import app
import requests


@app.task()
def status_check():
    r = requests.get('https://youtube.com')
    print(r.status_code)
