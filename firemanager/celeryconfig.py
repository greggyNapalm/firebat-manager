CELERY_IMPORTS = ("firemanager.tasks", )

BROKER_URL = 'sqla+sqlite:////tmp/celery-broker.sqlite'

CELERY_RESULT_BACKEND = "database"
CELERY_RESULT_DBURI = 'sqlite:////tmp/celery-backend.sqlite'
CELERY_TASK_RESULT_EXPIRES = 604800  # 1 weak.

CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
#CELERY_TIMEZONE = 'Europe/Oslo'
CELERY_ENABLE_UTC = True

## Enables error emails.
CELERY_SEND_TASK_ERROR_EMAILS = True
#
## Name and email addresses of recipients
ADMINS = (
    ("SupeHero", "batman@superman.me"),
)
#
## Email address used as sender (From field).
SERVER_EMAIL = "batman@superman.me"
#
## Mailserver configuration
EMAIL_HOST = "127.0.0.1"
EMAIL_PORT = 25
## EMAIL_HOST_USER = "servers"
## EMAIL_HOST_PASSWORD = "s3cr3t"
