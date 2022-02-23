from django.contrib import admin

# Register your models here.
from .models import Student,CourseOffering,Exam,Takes
examMan = [Student,CourseOffering,Exam,Takes]
admin.site.register(examMan)
admin.site.site_header = 'Exam Management'
