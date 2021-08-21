from django.db import models

# Create your models here.
class Domains(models.Model):
    fields = models.CharField(max_length=100)
    expertise = models.CharField(max_length=100)