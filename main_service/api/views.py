import time
from datetime import datetime
from random import choice

from rest_framework import viewsets
from django.http import JsonResponse

from cadastral.models import Query
from api.serializers import QuerySerializer, ResultSerializer


def external_query():
    print('external:')
    time.sleep(10)
    result = choice([True, False])
    print(result)
    return {'result': result}


class QueryViewSet(viewsets.ModelViewSet):
    queryset = Query.objects.all()
    serializer_class = QuerySerializer
    http_method_names = ['post']

    def perform_create(self, serializer):
        serializer.save(time_came=datetime.now())
        res = external_query()
        serializer.save(result_response=res['result'],
                        time_went=datetime.now())


class ResultViewSet(viewsets.ModelViewSet):
    queryset = Query.objects.all()
    serializer_class = ResultSerializer
