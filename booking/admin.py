from django.contrib import admin

# Register your models here.
from .models import Student,Feature,FeatureList,FeatureListToFeature,Room,GuideLine,Booking

class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'student_name', 'student_email')
    
class FeatureListToFeatureInLine(admin.StackedInline):
    model = FeatureListToFeature
    extra = 1
    
class FeatureListAdmin(admin.ModelAdmin):
    inlines=[FeatureListToFeatureInLine]
    
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'room_address')
    
class BookingAdmin(admin.ModelAdmin):
    list_display = ('create_time', 'name')
    
    
admin.site.register(Room,RoomAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(Feature)
admin.site.register(FeatureList,FeatureListAdmin)
admin.site.register(GuideLine)
admin.site.register(Booking,BookingAdmin)

#admin.site.register(FeatureListToFeature)