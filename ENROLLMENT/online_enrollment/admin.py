from django.contrib import admin
from .models import Student_info, Parrent_info, Course, Enrollment_info, Payment

# Register your models here.
admin.site.register(Student_info)
admin.site.register(Parrent_info)
admin.site.register(Course)
admin.site.register(Enrollment_info)
admin.site.register(Payment)
