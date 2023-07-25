from django.contrib import admin
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html
from .models import (
    Course,
    Batch,
    Comp_Brand,
    Trainer,
    Timings,
    Computer,
    Rooms,
    Student,
    Computer_Allocation,
)

# Register your models here.

admin.site.register(Course)


class BatchAdmin(admin.ModelAdmin):
    list_display = ("Batch_name", "Timeslot", "Course_Name")


admin.site.register(Batch, BatchAdmin)

admin.site.register(Comp_Brand)


class Traineradmin(admin.ModelAdmin):
    list_display = ("TrainerName", "Course")


admin.site.register(Trainer, Traineradmin)


class TimingAdmin(admin.ModelAdmin):
    list_display = ("Start_time", "End_time")


admin.site.register(Timings, TimingAdmin)


class ComputerAdmin(admin.ModelAdmin):
    list_display = ("Brand", "Type", "Assigned_trainer", "serial_number")


admin.site.register(Computer, ComputerAdmin)


class RoomsAdmin(admin.ModelAdmin):
    list_display = ("Room_name", "Room_type")


admin.site.register(Rooms, RoomsAdmin)


class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "Student_name",
        "Batch",
        "Trainer_Name",
        "Laptop_used",
        "view_course_link",
    )

    # def computer_allocation_link(self, obj):
    #     try:
    #         computer_allocation = Computer_Allocation.objects.get(Assigned_Student=obj)
    #         url = (
    #             reverse("admin:resources_computer_allocation_changelist")
    #             + f"?Assigned_Student__id__exact={obj.pk}"
    #         )
    #         return format_html('<a href="{}">Computer Allocation</a>', url)
    #     except Computer_Allocation.DoesNotExist:
    #         return "Not allocated"

    # computer_allocation_link.short_description = "Computer Allocation"
    
    def view_course_link(self, obj):
            # count = obj.district_set.count()
            # is_registered = Student.objects.get(id=obj.pk).isregistered
            if(obj.isregistered):
                url = (
                    reverse("admin:resources_computer_allocation_changelist")
                    + "?"
                    + urlencode({"resources": f"{obj.id}"})
                )
            # print(url)
                return format_html('<a href="{}">Go</a>', url)
            else:
                return " "


    view_course_link.allow_tags = True
    view_course_link.short_description = "Computer Allocation"

admin.site.register(Student, StudentAdmin)


# class allocationAdmin(admin.ModelAdmin):
#     list_display = ("Trainer", "Rooms", "Batch")


# class AllocationAdmin(admin.ModelAdmin):
#     list_display = ("Std_name", "Batch", "Trainer", "Laptop")


# admin.site.register(Computer_Allocation, AllocationAdmin)
