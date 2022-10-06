from django.contrib import admin
from .models import Student, Stud_details
from .models import Subject_wise_marks

admin.site.register(Student)
admin.site.register(Stud_details)
admin.site.register(Subject_wise_marks)