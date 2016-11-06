from rest_framework import serializers
from api.models import Hospital, Doctor


class HospitalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hospital
        fields = ('id', 'title', 'description', 'address', 'longitude', 'latitude', 'home_page', 'time_from', 'time_to')


class DoctorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Doctor
        fields = ('id', 'bio', 'first_name', 'last_name', 'email', 'phone', 'speciality')
