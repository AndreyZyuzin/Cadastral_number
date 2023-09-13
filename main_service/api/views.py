from datetime import datetime

import requests
from rest_framework import viewsets
from rest_framework import generics

from cadastral.models import Query
from api.serializers import QuerySerializer, ResultSerializer


EXTERNAL_RESULT = 'http://localhost:8001/result/'
EXTERNAL_PING = 'http://localhost:8001/'


class QueryViewSet(viewsets.ModelViewSet):
    queryset = Query.objects.all()
    serializer_class = QuerySerializer
    http_method_names = ['post']

    def perform_create(self, serializer):
        query = serializer.save(time_came=datetime.now())
        query_id = query.id
        print(serializer.data)
        res = requests.post(EXTERNAL_RESULT, data=serializer.data)
        res = res.json()
        query = Query.objects.get(id=query_id)
        print(f'res: {res.get("result")}')
        query.result_response = res.get('result')
        print(f'res: {datetime.now()}')
        query.time_went=datetime.now()
        query.save()


class ResultDetail(generics.RetrieveAPIView):
    queryset = Query.objects.all()
    serializer_class = ResultSerializer


class HistoryList(generics.ListAPIView):
    queryset = Query.objects.all()
    serializer_class = ResultSerializer