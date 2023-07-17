from django.contrib import admin
from .models import (
    Course,
    Batch,
    Comp_Brand,
    Trainer,
    Timings,
    Computer,
    Rooms,
    Computer_Allocation,
    Room_Allocation,
    Trainer_Allocation,
    Student
)

# Register your models here.


class BatchAdmin(admin.ModelAdmin):
    list_display = ('Batch_name', 'Timeslot', 'Course_Name')


class Traineradmin(admin.ModelAdmin):
    list_display = ('TrainerName', 'Course')


class TimingAdmin(admin.ModelAdmin):
    list_display = ('Start_time', 'End_time')


class ComputerAdmin(admin.ModelAdmin):
    list_display = ('Brand', 'Type', 'Assigned_trainer', 'serial_number')


class RoomsAdmin(admin.ModelAdmin):
    list_display = ('Room_name', 'Room_type')


class StudentAdmin(admin.ModelAdmin):
    list_display = ('Student_name', 'Batch', 'Trainer_Name', 'Laptop_used')


class CompAllocateAdmin(admin.ModelAdmin):
    list_display = ('Computer', 'Assigned_Student', 'Trainer')


class TrainerAllocateAdmin(admin.ModelAdmin):
    list_display = ('Trainer_Name', 'Room_Allocated', 'Timing', 'Batch_Name')


class RoomAllocateAdmin(admin.ModelAdmin):
    list_display = ('Room', 'Trainer_Name', 'Timeslot', 'Batch')


admin.site.register(Course)
admin.site.register(Batch, BatchAdmin)
admin.site.register(Comp_Brand)
admin.site.register(Trainer, Traineradmin)
admin.site.register(Timings, TimingAdmin)
admin.site.register(Computer, ComputerAdmin)
admin.site.register(Rooms, RoomsAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Computer_Allocation, CompAllocateAdmin)
admin.site.register(Trainer_Allocation, TrainerAllocateAdmin)
admin.site.register(Room_Allocation, RoomAllocateAdmin)
