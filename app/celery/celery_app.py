from celery import Celery

celery_app = Celery(
    "linkforge",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0",
)

# Celery-specific configuration
celery_app.conf.task_routes = {
    "app.celery.tasks.link.*": {"queue": "link_tasks"},
    "app.celery.tasks.analytics.*": {"queue": "analytics_tasks"},
}
