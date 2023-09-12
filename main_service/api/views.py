from datetime import datetime

import requests
from rest_framework import viewsets
from django.http import JsonResponse

from cadastral.models import Query
from api.serializers import QuerySerializer, ResultSerializer


EXTERNAL_RESULT = 'http://localhost:8001/result/'
EXTERNAL_PING = 'http://localhost:8001/'


class QueryViewSet(viewsets.ModelViewSet):
    queryset = Query.objects.all()
    serializer_class = QuerySerializer
    http_method_names = ['post']

    def perform_create(self, serializer):
        serializer.save(time_came=datetime.now())
        print(serializer.data)
        print('go')
        res = requests.post(EXTERNAL_RESULT, data=serializer.data)
        print(res)
        serializer.save(result_response=res['result'],
                        time_went=datetime.now())


class ResultViewSet(viewsets.ModelViewSet):
    queryset = Query.objects.all()
    serializer_class = ResultSerializer
