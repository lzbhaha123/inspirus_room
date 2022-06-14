from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('login_submit', views.login_submit, name='login_submit'),
    path('login_out', views.login_out, name='login_out'),
    path('registration', views.registration, name='registration'),
    path('registration_submit', views.registration_submit, name='registration_submit'),
    path('booking_room', views.booking_room, name='booking_room'),
    path('add_booking', views.add_booking, name='add_booking'),
    path('my_bookings', views.my_bookings, name='my_bookings'),
    path('cancel', views.cancel, name='cancel'),
    path('about', views.about, name='about'),
]