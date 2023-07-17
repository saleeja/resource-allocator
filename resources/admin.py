from django.contrib import admin
from .models import (
    Course,
    Batch,
    Comp_Brand,
    Trainer,
    Timings,
    Computer,
    Rooms,
    Student,
)

# Register your models here.

admin.site.register(Course)

class BatchAdmin(admin.ModelAdmin):
    list_display = ('Batch_name', 'Timeslots', 'Course_Name')
admin.site.register(Batch,BatchAdmin)

admin.site.register(Comp_Brand)

class Traineradmin(admin.ModelAdmin):
    list_display = ('Trainer_Name', 'Course')
admin.site.register(Trainer, Traineradmin)

class TimingAdmin(admin.ModelAdmin):
    list_display = ('Start_time', 'End_time')
admin.site.register(Timings, TimingAdmin)

class ComputerAdmin(admin.ModelAdmin):
    list_display = ('Brand', 'Type', 'Assigned_trainer', 'serial_number')
admin.site.register(Computer, ComputerAdmin)

class RoomsAdmin(admin.ModelAdmin):
    list_display = ('Room_name', 'Room_type')
admin.site.register(Rooms,RoomsAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('Std_name', 'Batch', 'Trainer', 'Laptop')
admin.site.register(Student, StudentAdmin)

