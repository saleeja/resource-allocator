from django.db import models

# Create your models here.

ownership = ((0, "owned"), (1, "rented"))


class Course(models.Model):
    Course = models.CharField(max_length=220)

    def __str__(self):
        return self.Course

    class Meta:
        verbose_name_plural = "Courses"


class Trainer(models.Model):
    TrainerName = models.CharField(max_length=220)
    Course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.TrainerName

    class Meta:
        verbose_name_plural = "Trainers"


class Timings(models.Model):
    Timeslots = models.CharField(max_length=220)

    def __str__(self):
        return self.Timeslots

    class Meta:
        verbose_name_plural = "Timings"


class Batch(models.Model):
    Batch_name = models.CharField(max_length=220)
    Timeslots = models.ForeignKey(Timings, on_delete=models.CASCADE)

    def __str__(self):
        return self.Batch_name

    class Meta:
        verbose_name_plural = "Batches"


class Comp_Brand(models.Model):
    Brand = models.CharField(max_length=100)

    def __str__(self):
        return self.Brand

    class Meta:
        verbose_name_plural = "Computer Brands"


class Laptop(models.Model):
    Lap_code = models.CharField(max_length=50)
    Lap_brand = models.ForeignKey(Comp_Brand, on_delete=models.CASCADE)
    Lap_ownership = models.IntegerField(choices=ownership, null=False)

    def __str__(self):
        return self.Lap_code

    class Meta:
        verbose_name_plural = "Laptops"


class Desktop(models.Model):
    Desk_code = models.CharField(max_length=50)
    Desk_brand = models.ForeignKey(Comp_Brand, on_delete=models.CASCADE)
    Desk_ownership = models.IntegerField(choices=ownership, null=False)

    def __str__(self):
        return self.Desk_code

    class Meta:
        verbose_name_plural = "Desktops"


class Classrooms(models.Model):
    cls_Rooms = models.CharField(max_length=100)

    def __str__(self):
        return self.cls_Rooms

    class Meta:
        verbose_name_plural = "Classrooms"


class Conference_rooms(models.Model):
    cnfrnc_rooms = models.CharField(max_length=100)

    def __str__(self):
        return self.cnfrnc_rooms

    class Meta:
        verbose_name_plural = "Conference Rooms"


# class Rooms(models.Model):
#     cls_room = models.ForeignKey(Classrooms, on_delete=models.CASCADE)
#     cnfrnc_room = models.ForeignKey(Conference_rooms, on_delete=models.CASCADE)

#     class Meta:
#         verbose_name_plural = "Rooms"


