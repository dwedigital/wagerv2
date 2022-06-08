# from masonite.environment import env


DRIVERS = {
    "default": "amqp",
    "database": {
        "connection": "sqlite",
        "table": "jobs",
        "failed_table": "failed_jobs",
        "attempts": 3,
        "poll": 5,
    },
    "redis": {
        #
    },
    "amqp": {
        "username": "ybengqzn",
        "password": "0NQeWSyNPWP59viUIGqUpxnr7au5DiST",
        "port": "5672",
        "vhost": "ybengqzn",
        "host": "rattlesnake.rmq.cloudamqp.com",
        "channel": "",
        "connection_options": {},
        "exchange": "",
        "queue": "default",
        "tz":"UTC",
    },
    "async": {
        "blocking": False,
        "callback": "handle",
        "mode": "threading",
        "workers": 1,
    },
}
