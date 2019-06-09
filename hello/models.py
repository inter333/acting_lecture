import datetime
from django.db import models
from django.utils import timezone

subjects = [
            ('国語','国語'),
            ('数学','数学'),
            ('英語','英語'),
            ('理科','理科'),
            ('社会','社会')
        ]

times = [
    ('10:50','10:50'),
    ('12:50','12:50'),
    ('14:20','14:20'),
    ('15:50','15:50'),
    ('17:20','17:20'),
    ('18:50','18:50'),
    ('20:20','20:20'),
]

grades = [
    ('小1','小1'),
    ('小2','小2'),
    ('小3','小3'),
    ('小4','小4'),
    ('小5','小5'),
    ('小6','小6'),
    ('中1','中1'),
    ('中2','中2'),
    ('中3','中3'),
    ('高１','高１'),
    ('高2','高2'),
    ('高3','高3'),
]

class Users(models.Model):
    name=models.CharField(max_length=100)
    mail=models.EmailField(max_length=200)
    passward=models.CharField(max_length=100)
    

    def __str__(self):
        return self.name


class Classes(models.Model):
    date    = models.DateField()
    time    = models.TimeField(choices=times)
    name    = models.CharField(max_length=100)
    grade   = models.CharField(choices=grades,max_length=100)
    subject = models.CharField(choices=subjects,max_length=100)
    remark  = models.CharField(max_length=100)
    act_user = models.CharField(max_length=100)

    def __str__(self):
        return self.subject


class Act_person(models.Model):
    act_person_name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.act_person_name
    

# Create your models here.
