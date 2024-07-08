from django.contrib import admin
from .models import VaccinationCenter,VaccinationSlot


admin.site.register(VaccinationSlot)
admin.site.register(VaccinationCenter)