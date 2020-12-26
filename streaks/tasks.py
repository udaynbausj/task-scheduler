from task_scheduler.celery import app
import time


@app.task()
def invalidate_streaks(counter):
    time.sleep(10)
    print("done")
