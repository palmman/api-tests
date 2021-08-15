from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import Symptom, Measurement

# Register your models here.



class SymptomAdmin(admin.ModelAdmin):
    pass

admin.site.register(Symptom, SymptomAdmin)



class MeasurementAdmin(admin.ModelAdmin):

    list_display = ['user', 'created', 'temperature', 'o2sat', 'systolic', 'diastolic', 'symptom_display']
    list_filter = ['user', 'created']
    filter_horizontal = ['symptoms',]

admin.site.register(Measurement, MeasurementAdmin)