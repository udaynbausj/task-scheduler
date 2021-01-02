config = {
    "broker_url": "amqp://guest@localhost:5672",
    "task_routes": {
        "streaks.tasks.*": "streaks",
    },
}
