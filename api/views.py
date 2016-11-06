from django.shortcuts import render
from rest_framework import viewsets
from api.models import *
from api.serializers import *


# Create your views here.
class HospitalView(viewsets.ModelViewSet):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer


class DoctorView(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
