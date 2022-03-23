import logging
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from booking.models import Student
from django.core import serializers


def index(request):
     student_id = None
     try:
          student_id = request.session['student_id']
     except:
          pass
     
     return render(request, 'booking/index.html', {'student_id':student_id})

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
     return HttpResponse(user_data.student_id)

def login_out(request):
     request.session['student_id'] = None
     request.session['student_name'] = None
     request.session['student_email'] = None
     return HttpResponseRedirect("./")
     