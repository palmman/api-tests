from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class Symptom(models.Model):

    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Measurement(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    temperature = models.DecimalField(max_digits=4, decimal_places=2, help_text='อุณหภูมิ')
    o2sat = models.IntegerField(help_text='o2 ในเลือด')
    systolic = models.IntegerField(help_text='ความดันตัวบน')
    diastolic = models.IntegerField(help_text='ความดันตัวล่าง')
    symptoms = models.ManyToManyField(Symptom, blank=True, help_text='อาการที่พบ')

    @property
    def symptom_display(self):
        return ', '.join(self.symptoms.values_list('name', flat=True))

    class Meta:
        ordering = ['-created']


