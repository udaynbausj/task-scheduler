from .celery import app
import time


@app.task(bind=True)
def add(x, y):
    time.sleep(10)
    return x + y
