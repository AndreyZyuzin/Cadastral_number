from django.urls import path

from api.views import QueryViewSet, ResultDetail, HistoryList

urlpatterns = [
    path('query/', QueryViewSet.as_view({'post': 'create'}), name='query'),
    path('result/<int:pk>/', ResultDetail.as_view(), name='result_detail'),
    path('history/', HistoryList.as_view(), name='history_list')
]
