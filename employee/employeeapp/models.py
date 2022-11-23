from django.db import models

# Create your models here.


class employee(models.Model):
    name = models.CharField(max_length=70)
    salary = models.IntegerField()
    designation = models.CharField(max_length=70)
    company = models.CharField(max_length=70)
