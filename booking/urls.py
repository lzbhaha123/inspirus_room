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
]