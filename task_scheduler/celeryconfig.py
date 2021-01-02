from .beat import config as beat_config

config = {
    "broker_url": "amqp://guest@localhost:5672",
    "task_routes": {
        "streaks.tasks.*": "streaks",
        "ping.tasks.*": "ping",
    },
    "beat_schedule": beat_config
}
