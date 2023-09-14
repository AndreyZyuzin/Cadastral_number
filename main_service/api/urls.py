from django.urls import path

from api.views import (HistoryList, PingDetail, QueryDetail, QueryViewSet,
                       ResultDetail)

urlpatterns = [
    path('query2/', QueryViewSet.as_view({'post': 'create'}), name='query'),
    path('query/', QueryDetail.as_view(), name='query_detail'),
    path('result/<int:pk>/', ResultDetail.as_view(), name='result_detail'),
    path('history/', HistoryList.as_view(), name='history_list'),
    path('ping/', PingDetail.as_view()),
]
