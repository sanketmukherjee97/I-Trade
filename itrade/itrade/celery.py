import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'itrade.settings')

app = Celery('itrade')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'get_stock_data_30': {
        'task': 'trade.dashboard.tasks.get_stock_data',
        'schedule': 30.0
    }
}

app.autodiscover_tasks()
