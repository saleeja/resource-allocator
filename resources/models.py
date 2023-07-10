from django.db import models

# Create your models here.

ownership = ((0, "owned"), (1, "rented"))
category = ((0, "Laptop"), (1, "Desktop"))
room_type = ((0, "Classroom"), (1, "Conference Rooms"))


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


# class Timings(models.Model):

#     Start_time = models.TimeField()
#     End_time = models.TimeField()

#     def __str__(self):
#         return self.Start_time, self.End_time

#     class Meta:
#         verbose_name_plural = "Timings"


class Batch(models.Model):
    Batch_name = models.CharField(max_length=220)
    # Timeslots = models.ForeignKey(Timings, on_delete=models.CASCADE)

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


class Computer(models.Model):
    Comp_code = models.CharField(max_length=50)
    Category = models.IntegerField(choices=category, null=False)
    Brand = models.ForeignKey(Comp_Brand, on_delete=models.CASCADE)
    Type = models.IntegerField(choices=ownership, null=False)
    Assigned_trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)

    def __str__(self):
        return self.Comp_code

    class Meta:
        verbose_name_plural = "Computers"


class Rooms(models.Model):
    Room_name: models.CharField(max_length=100)
    Room_type: models.IntegerField(choices=room_type, null=False)

    def __str__(self):
        return self.Room_name

    class Meta:
        verbose_name_plural = "Rooms"
