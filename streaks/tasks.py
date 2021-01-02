from task_scheduler.celery import app
import time


@app.task()
def invalidate_streaks(counter):
    time.sleep(10)
    for i in range(10):
        print("done")


@app.task()
def health():
    time.sleep(10)
    print("health is fine. this is from worker")
