from statistics import mode
from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.CharField(max_length=12)
    student_name = models.CharField(max_length=50)
    student_email = models.CharField(max_length=50)
    student_password= models.CharField(max_length=25)
