from datetime import datetime

import requests
from celery import shared_task

from cadastral.models import Query


@shared_task()
def request_post_external_server(url, data, id):
    """Запрос внешнего сервера."""
    res = requests.post(url, data)
    res = res.json()
    query = Query.objects.get(id=id)
    query.result_response = res.get('result')
    query.time_went = datetime.now()
    query.save()
