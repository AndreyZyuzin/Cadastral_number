from rest_framework import serializers

from cadastral.models import Query


class QuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Query
        fields = '__all__'
        read_only_fields = ('time_came',)


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Query
        fields = ('cadastral_number', 'latitude', 'longitude')
