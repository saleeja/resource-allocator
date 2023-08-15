from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode
from django.http import HttpResponseRedirect
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
    Student,
)

# Register your models here.


class BatchAdmin(admin.ModelAdmin):
    list_display = ("Batch_name", "Timeslot", "Course_Name")


class Traineradmin(admin.ModelAdmin):
    list_display = ("TrainerName", "Course")


class TimingAdmin(admin.ModelAdmin):
    list_display = ("Start_time", "End_time")


class ComputerAdmin(admin.ModelAdmin):
    list_display = ("Brand", "Type", "Assigned_trainer", "serial_number")


class RoomsAdmin(admin.ModelAdmin):
    list_display = ("Room_name", "Room_type")


class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "Student_name",
        "Batch",
        "Trainer_Name",
        "Laptop_used",
        "computer_allocation_link",
    )

    def computer_allocation_link(self, obj):
        link = reverse(
            "admin:%s_%s_add"
            % (obj._meta.app_label, Computer_Allocation._meta.model_name)
        )
        link += f"?Assigned_Student={obj.pk}&Trainer={obj.Trainer_Name.pk}"
        return format_html('<a href="{}">Allocate Computer</a>', link)

    computer_allocation_link.short_description = "Computer Allocation"


class CompAllocateAdmin(admin.ModelAdmin):
    list_display = ("Computer", "Assigned_Student", "Trainer")

    def response_add(self, request, obj, post_url_continue=None):
        if "_addanother" not in request.POST:
            return HttpResponseRedirect(
                reverse(
                    "admin:%s_%s_changelist"
                    % (obj._meta.app_label, Student._meta.model_name)
                )
            )

        return super().response_add(request, obj, post_url_continue)

        # Override the response after adding a new Computer_Allocation entry
        # if "_addanother" not in request.POST:
        #     # If the "Save and add another" button is not pressed,
        #     # redirect back to the "Student" table view.
        #     student_id = request.POST.get("Assigned_Student")
        #     if student_id:
        #         url = reverse(
        #             "admin:%s_%s_change"
        #             % (obj._meta.app_label, Student._meta.model_name),
        #             args=[student_id],
        #         )
        #         query_string = urlencode({"Computer_Allocation__id__exact": obj.id})
        #         url = "{}?{}".format(url, query_string)
        #         return HttpResponseRedirect(url)

        # return super().response_add(request, obj, post_url_continue)


class TrainerAllocateAdmin(admin.ModelAdmin):
    list_display = ("Trainer_Name", "Room_Allocated", "Timing", "Batch_Name")


class RoomAllocateAdmin(admin.ModelAdmin):
    list_display = ("Room", "Trainer_Name", "Timeslot", "Batch")


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
