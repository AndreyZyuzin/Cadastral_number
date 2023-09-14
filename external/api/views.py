import time
from random import choice, randint

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

MIN_DELAY = 20
MAX_DELAY = 60


@api_view(['POST'])
def result(request):
    time.sleep(randint(MIN_DELAY, MAX_DELAY))
    result = choice([True, False])
    return Response({'result': result}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def ping(request):
    return Response(status=status.HTTP_200_OK)
