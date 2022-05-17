import logging
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from booking.models import Student,Room,Booking
from django.core import serializers
from django.http import JsonResponse
from datetime import datetime
import json


def index(request):
     try:
          student_id = request.session['student_id']
          student_name = request.session['student_name']
     except:
          pass
     
     room_list = Room.objects.order_by('room_id')
     
     return render(request, 'booking/index.html', {'student_id':student_id,'student_name':student_name,'room_list':room_list})

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

def booking_room(request):
     room_id = request.GET.get("roomid")
     try:
          student_id = request.session['student_id']
          student_name = request.session['student_name']
     except:
          pass
     #return HttpResponse(room_id)
     #room = Room.objects.get(room_id=room_id)
     bookings = Booking.objects.filter(room=Room.objects.get(room_id=room_id))
     
     return render(request, 'booking/booking_room.html', {'student_id':student_id,'student_name':student_name,"bookings":serializers.serialize("json", bookings)})

def add_booking(request):
     room_id = request.POST.get("roomId")
     start = request.POST.get("start")
     end = request.POST.get("end")
     student_id = ""
     try:
          student_id = request.session['student_id']
     except:
         return JsonResponse({"login":True}, status=200)
     if student_id=="":
          return JsonResponse({"login":True}, status=200)
     student_obj = Student.objects.get(student_id = student_id)
     room_obj = Room.objects.get(room_id = room_id)
     new_booking = Booking(name="booking test",start_time=start,end_time=end,create_time=datetime.now(),confirm=False,student=student_obj,room=room_obj)
     new_booking.save()
     
     return JsonResponse({"type":True}, status=200)