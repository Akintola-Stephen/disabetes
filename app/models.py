# -*- encoding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#123ABCDE

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    dob = models.DateField()
    gender = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    pregnancy = models.IntegerField(null=True)
    glucose = models.IntegerField(null=True)
    blood_pressure = models.IntegerField(null=True)
    skin_thickness = models.IntegerField(null=True)
    insulin = models.IntegerField(null=True)
    bmi = models.IntegerField(null=True)
    pedigree = models.IntegerField(null=True)
    age = models.IntegerField(null=True)
    predicted_result = models.BooleanField(default=False)

