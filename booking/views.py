import logging
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from booking.models import Student
from django.core import serializers


def index(request):
     try:
          student_id = request.session['student_id']
          student_name = request.session['student_name']
     except:
          pass
     
     return render(request, 'booking/index.html', {'student_id':student_id,'student_name':student_name})

def login(request):
     return render(request, 'booking/login.html', {})

def login_submit(request):
     user_data = None
     try:
          user_data = Student.objects.get(student_id=request.POST.get("studentId"),student_password=request.POST.get("password"))
     except:
          return HttpResponse("No student")
     
     request.session['student_id'] = user_data.student_id
     request.session['student_name'] = user_data.student_name
     request.session['student_email'] = user_data.student_email
     return HttpResponseRedirect("./")

def login_out(request):
     request.session['student_id'] = None
     request.session['student_name'] = None
     request.session['student_email'] = None
     return HttpResponseRedirect("./")

def registration(request):

     return render(request, 'booking/registration.html', {})

def registration_submit(request):
     new_user = Student(student_id=request.POST.get("studentId"),
                        student_name=request.POST.get("studentName"),
                        student_email=request.POST.get("email"),
                        student_password=request.POST.get("password"))
     new_user.save()

     
     return HttpResponseRedirect("./login")