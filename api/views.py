from django.shortcuts import render
from rest_framework import viewsets
from api.models import Hospital
from api.serializers import HospitalSerializer


# Create your views here.
class HospitalViewSet(viewsets.ModelViewSet):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer
