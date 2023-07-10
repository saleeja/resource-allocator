from django.contrib import admin
from .models import (
    Course,
    Batch,
    Comp_Brand,
    Trainer,
    # Timings,
    Computer,
    Rooms,
)

# Register your models here.


class Adminnn(admin.ModelAdmin):
    title = ["", "", ""]


admin.site.register(Course, Adminnn)
admin.site.register(Batch)
admin.site.register(Comp_Brand)
admin.site.register(Trainer)
# admin.site.register(Timings)
admin.site.register(Computer)
admin.site.register(Rooms)
