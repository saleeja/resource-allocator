from django.contrib import admin
from .models import Course, Batch, Comp_Brand, Trainer, Timings, Laptop, Desktop


# Register your models here.

admin.site.register(Course)
admin.site.register(Batch)
admin.site.register(Comp_Brand)
admin.site.register(Trainer)
admin.site.register(Timings)
admin.site.register(Laptop)
admin.site.register(Desktop)
