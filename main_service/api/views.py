from datetime import datetime

import requests
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings

from cadastral.models import Query
from api.serializers import QuerySerializer, ResultSerializer
from api.tasks import request_post_external_server


class QueryViewSet(viewsets.ModelViewSet):
    queryset = Query.objects.all()
    serializer_class = QuerySerializer
    http_method_names = ['post']

    def perform_create(self, serializer):
        query = serializer.save(time_came=datetime.now())
        query_id = query.id
        print(serializer.data)
        res = requests.post(settings.EXTERNAL_RESULT, data=serializer.data)
        res = res.json()
        query = Query.objects.get(id=query_id)
        print(f'res: {res.get("result")}')
        query.result_response = res.get('result')
        print(f'res: {datetime.now()}')
        query.time_went=datetime.now()
        query.save()


class QueryDetail(generics.CreateAPIView):
    queryset = Query.objects.all()
    serializer_class = QuerySerializer

    def post(self, request):
        serializer = QuerySerializer(data=request.data)
        if serializer.is_valid():
            query = serializer.save(time_came=datetime.now())

            request_post_external_server.delay(
                url=settings.EXTERNAL_RESULT,
                data=serializer.data, id=query.id
            )

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResultDetail(generics.RetrieveAPIView):
    queryset = Query.objects.all()
    serializer_class = ResultSerializer


class HistoryList(generics.ListAPIView):
    queryset = Query.objects.all()
    serializer_class = ResultSerializer


class PingDetail(generics.RetrieveAPIView):
    def get(self, request):
        try:
            res = requests.get(settings.EXTERNAL_PING)
            print(res)
            print(res.status_code)
            if res.status_code == status.HTTP_200_OK:
                return Response('Ok')
            else:
                return Response(f'Fail!!! {settings.EXTERNAL_PING} '
                                f'{res.status_code}')
        except requests.exceptions.ConnectionError:
            return Response(f'Нет связи с {settings.EXTERNAL_PING}')
