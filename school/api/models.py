from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    inclass = models.IntegerField()
    roll = models.IntegerField()
    age = models.IntegerField()


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    age = models.IntegerField()    