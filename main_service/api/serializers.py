from rest_framework import serializers

from cadastral.models import Query


class QuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Query
        fields = '__all__'
        read_only_fields = ('time_came', 'time_went', 'result_response')


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Query
        exclude = ('id',)
