from django.contrib import admin

# Register your models here.
from .models import Student,Feature,FeatureList,FeatureListToFeature

class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'student_name', 'student_email')

admin.site.register(Student,StudentAdmin)
admin.site.register(Feature)
admin.site.register(FeatureList)
admin.site.register(FeatureListToFeature)