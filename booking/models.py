from statistics import mode
from xml.parsers.expat import model
from django.db import models
from datetime import datetime
import pytz

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
    feature_count = models.IntegerField()
    
class GuideLine(models.Model):
    guideline_id = models.AutoField(primary_key=True)
    name =  models.CharField(max_length=25)
    content =  models.CharField(max_length=255)
    def __str__(self):
        return self.content
    
class Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    name =  models.CharField(max_length=25)
    room_address =  models.CharField(max_length=255)
    feature_list = models.ForeignKey(FeatureList,on_delete=models.SET_NULL,null=True)
    guideline = models.ForeignKey(GuideLine,on_delete=models.SET_NULL,null=True)
    other_detail =  models.CharField(max_length=255)
    qe_code_url =  models.CharField(max_length=255)
    picture = models.CharField(max_length=50,default="")
    def feature_detail(self):
        return FeatureListToFeature.objects.filter(feature_list=self.feature_list)
        
    def __str__(self):
        return self.name
    
class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    name =  models.CharField(max_length=50)
    start_time =  models.CharField(max_length=50)
    end_time =  models.CharField(max_length=50)
    create_time =  models.CharField(max_length=50)
    confirm = models.BooleanField(default=False)
    student = models.ForeignKey(Student,on_delete=models.SET_NULL,null=True)
    room = models.ForeignKey(Room,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return self.name
    def period(self):
        NZST = pytz.timezone('Pacific/Auckland')
        f = datetime.strptime(self.start_time,"%Y-%m-%d %H:%M:%S") # datetime.fromtimestamp(int(self.start_time[0:10]))
        s = datetime.strptime(self.end_time,"%Y-%m-%d %H:%M:%S") #datetime.fromtimestamp(int(self.end_time[0:10]))
        
        f = f.astimezone(NZST)
        s = s.astimezone(NZST)
        return datetime.strftime(f,"%d %b %H:%M") +" --- " + datetime.strftime(s,"%d %b %H:%M") #str(datetime.strftime(f,"%d %b %H:%M")) +" --- " + str(datetime.strftime(s,"%d %b %H:%M"))
    def room_name(self):
        return self.room.name
    def student_name(self):
        return self.student.student_name
    def student_id(self):
        return self.student.student_id
    def booking_time(self):
        return self.create_time.split(".")[0]
    
    