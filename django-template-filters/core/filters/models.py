from django.db import models

# Create your models here.
class date_of(models.Model):
    date1=models.DateField(auto_now=True)
    date2=models.DateTimeField(auto_now_add=True)