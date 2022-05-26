import logging
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from booking.models import Student,Room,Booking,Feature,FeatureList,FeatureListToFeature
from django.core import serializers
from django.http import JsonResponse
from datetime import datetime
from django.core.paginator import Paginator

def index(request):
     student_id = None
     student_name = None
     room_list = None
     try:
          student_id = request.session['student_id']
          student_name = request.session['student_name']
     except:
          pass
     
     if (request.POST.get("info")!="" and request.POST.get("info")!=None):
          try:
               info = request.POST.get("info")
               room_list = Room.objects.order_by('room_id').filter(name__contains=info) | Room.objects.order_by('room_id').filter(room_address__contains=info)
               
          except:
               pass
     else:
          try:
               room_list = Room.objects.order_by('room_id')
          except:
               pass

     v = ""
     features = Feature.objects.all()
     
     checks = []
     for f in features:
          if(request.POST.get("featurecheck"+str(f.feature_id))!=None):
               checks.append(request.POST.get("featurecheck"+str(f.feature_id)))
     if len(checks):
          ff = FeatureListToFeature.objects.filter(feature__in=checks)
          fl = []
          for f in ff:
               fl.append(f.feature_list)
          #return HttpResponse(fl)  
          if room_list == None:
               room_list = Room.objects.filter(feature_list__in = fl)
          else:
               room_list = room_list.filter(feature_list__in = fl)
     return render(request, 'booking/index.html', {'features':features,'student_id':student_id,'student_name':student_name,'room_list':room_list})

def login(request):
     return render(request, 'booking/login.html', {})

def login_submit(request):
     user_data = None
     try:
          user_data = Student.objects.get(student_id=request.POST.get("studentId"),student_password=request.POST.get("password"))
     except:
          return render(request, 'booking/login.html', {})
     
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
     student_id = None
     student_name = None
     try:
          student_id = request.session['student_id']
          student_name = request.session['student_name']
     except:
          pass
     
     room = Room.objects.get(room_id = room_id)
     bookings = Booking.objects.filter(room=Room.objects.get(room_id=room_id))
     for obj in bookings:
          obj.start_time = str(int(datetime.timestamp(datetime.strptime(obj.start_time,"%Y-%m-%d %H:%M:%S"))))+"000"
          obj.end_time = str(int(datetime.timestamp(datetime.strptime(obj.end_time,"%Y-%m-%d %H:%M:%S"))))+"000"

     return render(request, 'booking/booking_room.html', {'room':room,'student_id':student_id,'student_name':student_name,"bookings":serializers.serialize("json", bookings)})

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
     start = datetime.fromtimestamp(int(start[0:10]))
     end = datetime.fromtimestamp(int(end[0:10]))
     new_booking = Booking(name="booking test",start_time=start,end_time=end,create_time=datetime.now(),confirm=False,student=student_obj,room=room_obj)
     new_booking.save()
     
     return JsonResponse({"type":True}, status=200)


def my_bookings(request):
     student_id = None
     student_name = None
     try:
          student_id = request.session['student_id']
          student_name = request.session['student_name']
          bookings = Booking.objects.filter(student=Student.objects.get(student_id=student_id)).values("booking_id","room__name","start_time","end_time","confirm")
          paginator = Paginator(bookings, 20)
          page_number = request.GET.get('page')
          page_obj = paginator.get_page(page_number)
          return render(request, 'booking/my_bookings.html',{'page_obj':page_obj,'bookings':bookings,'student_id':student_id,'student_name':student_name})
     except:
          pass
     return render(request, 'booking/my_bookings.html',{'student_id':student_id,'student_name':student_name})

def cancel(request):
     id = request.GET.get('id')
     Booking.objects.get(booking_id = id).delete()
     return HttpResponseRedirect("./my_bookings")