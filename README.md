#Task-Scheduler
Tasks which are cpu intensive and doesn't need an immediate
response can be processed in background. For example, generating Pdf
files. User might not expect the Pdf generation in real-time. So,
we can leverage the performance of task-queues for such scenarios.

Queues have other advantages like persistence, reliability,
decoupling.<br>


This repo is one such example which fakes cpu intensive tasks and
sends the task to queue. Here we use RabbitMq as broker. Celery is being
used in this repo. Celery provides apis for task-queues and 
supports distributed environment.Used Django as framework.<br>

##Dependencies
Python - 3.9<br>
Django - 3.1<br>
Celery - 5.0<br>
RabbitMq - 3.8.9

##Commands
``$ celery -A task_scheduler worker -Q {queue_name} ``<br>
``$ python manage.py runserver``

###Note
We need to run Django Server as well as celery worker.
