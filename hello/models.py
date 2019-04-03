import datetime
from django.db import models
from django.utils import timezone

class Users(models.Model):
    name=models.CharField(max_length=100)
    mail=models.EmailField(max_length=200)
    passward=models.CharField(max_length=100)
    

    def __str__(self):
        return self.name


class Classes(models.Model):
    date    = models.DateField()
    time    = models.TimeField()
    name    = models.CharField(max_length=100)
    grade   = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    remark  = models.CharField(max_length=100)

    def __str__(self):
        return self.subject


class Act_person(models.Model):
    act_person_name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.act_person_name
    

# Create your models here.
