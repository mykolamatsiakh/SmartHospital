from rest_framework import serializers
from api.models import Hospital, Doctor, Patient


class HospitalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hospital
        fields = [
            'id', 'title', 'description', 'address', 'longitude', 'latitude', 'home_page', 'time_from', 'time_to','image'
            ]


class DoctorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Doctor
        fields = ('id', 'bio', 'first_name', 'last_name', 'email', 'phone', 'speciality')


class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields = ('id','first_name', 'last_name', 'email', 'phone')

