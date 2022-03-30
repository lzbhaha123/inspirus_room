from statistics import mode
from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.CharField(primary_key=True,max_length=12)
    student_name = models.CharField(max_length=50)
    student_email = models.CharField(max_length=50)
    student_password= models.CharField(max_length=25)
    def __str__(self):
        return self.student_id
    
class Feature(models.Model):
    feature_id = models.AutoField(primary_key=True)
    name =  models.CharField(max_length=25)
    def __str__(self):
        return self.name
    
class FeatureList(models.Model):
    feature_list_id = models.AutoField(primary_key=True)
    name =  models.CharField(max_length=25)
    def __str__(self):
        return self.name
    
class FeatureListToFeature(models.Model):
    feature_list =  models.ForeignKey(FeatureList,on_delete=models.CASCADE)
    feature = models.ForeignKey(Feature,on_delete=models.CASCADE)
    feature_count = models.IntegerField(max_length=25)