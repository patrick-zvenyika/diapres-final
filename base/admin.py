from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(PatientData)
admin.site.register(EarlyDiagnosisPatient)
admin.site.register(ChatMessage)