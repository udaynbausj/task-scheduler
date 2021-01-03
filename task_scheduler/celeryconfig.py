from .beat import config as beat_config
from kombu import Queue

config = {
    "broker_url": "amqp://guest@localhost:5672",
    "task_routes": {
        # here routing_key means a key which is attached to message. queue will consume
        # the message if queue's binding_key is same as message's routing_key
        "ping.tasks.status_check": {
            'queue': 'ping.tasks.status_check',
            'routing_key': 'ping.tasks.status_check',
        },
        "streaks.tasks.health": {
            'queue': 'streaks.tasks.health',
            'routing_key': 'streaks.tasks.health'
        },
    },
    "task_queues": {
        # here routing_key refers to  binding_key. Queue will only get messages from some exchange, if
        # messages has routing_key same as queue's binding_key
        Queue(name='ping.tasks.status_check', routing_key='ping.tasks.status_check'),
        Queue(name='streaks.tasks.health', routing_key='streaks.tasks.health')
    },
    "beat_schedule": beat_config
}
