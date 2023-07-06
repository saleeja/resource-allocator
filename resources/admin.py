from django.contrib import admin
from .models import (
    Course,
    Batch,
    Comp_Brand,
    Trainer,
    Timings,
    Laptop,
    Desktop,
    Conference_rooms,
    Classrooms,
)

# Register your models here.


class Adminnn(admin.ModelAdmin):
    title = ["", "", ""]


admin.site.register(Course, Adminnn)
admin.site.register(Batch)
admin.site.register(Comp_Brand)
admin.site.register(Trainer)
admin.site.register(Timings)
admin.site.register(Laptop)
admin.site.register(Desktop)
admin.site.register(Conference_rooms)
admin.site.register(Classrooms)
