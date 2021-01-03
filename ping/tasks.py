from task_scheduler.celery import app
import requests
import time


@app.task()
def status_check():
    time.sleep(10)
    r = requests.get('https://youtube.com')
    print(r.status_code)
