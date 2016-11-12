from django.contrib import admin
from api.models import Hospital, Doctor, Patient

# Register your models here.
admin.site.register(Hospital)
admin.site.register(Doctor)
admin.site.register(Patient)