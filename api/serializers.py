from rest_framework import serializers
from api.models import Hospital


class HospitalSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Hospital
        fields = (
            'id', 'title', 'description', 'address', 'longitude', 'latitude', 'home_page', 'time_from', 'time_to',
            'photo')
