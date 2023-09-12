from datetime import datetime

from rest_framework import viewsets
from django.http import JsonResponse

from cadastral.models import Query
from api.serializers import QuerySerializer, ResultSerializer


class QueryViewSet(viewsets.ModelViewSet):
    queryset = Query.objects.all()
    serializer_class = QuerySerializer
    http_method_names = ['post']

    def perform_create(self, serializer):
        serializer.save(time_came=datetime.now())
        res = {'result': 42}
        serializer.save(result_response=res['result'],
                        time_went=datetime.now())


class ResultViewSet(viewsets.ModelViewSet):
    queryset = Query.objects.all()
    serializer_class = ResultSerializer
