from django.db import models

# Create your models here.

ownership = ((0, "owned"), (1, "rented"))


class Course(models.Model):
    Course = models.CharField(max_length=220)

    def __str__(self):
        return self.Course
    class Meta:
        verbose_name_plural="Courses"



class Trainer(models.Model):
    TrainerName = models.CharField(max_length=220)
    Course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.TrainerName
    class Meta:
        verbose_name_plural="Trainers"



class Timings(models.Model):
    Timeslots = models.CharField(max_length=220)

    def __str__(self):
        return self.Timeslots
    class Meta:
        verbose_name_plural="Timings"



class Batch(models.Model):
    Batch_name = models.CharField(max_length=220)
    Timeslots = models.ForeignKey(Timings, on_delete=models.CASCADE)

    def __str__(self):
        return self.Batch_name
    class Meta:
        verbose_name_plural="Batches"



class Comp_Brand(models.Model):
    Brand = models.CharField(max_length=100)

    def __str__(self):
        return self.Brand
    class Meta:
        verbose_name_plural="Computer Brands"



class Laptop(models.Model):
    Lap_code = models.IntegerField()
    Lap_brand = models.ForeignKey(Comp_Brand, on_delete=models.CASCADE)
    Lap_ownership = models.IntegerField(choices=ownership, null=False)

    # def __str__(self):
    #     return self.Lap_brand
    class Meta:
        verbose_name_plural="Laptops"



class Desktop(models.Model):
    Desk_code = models.IntegerField()
    Desk_brand = models.ForeignKey(Comp_Brand, on_delete=models.CASCADE)
    Desk_ownership = models.IntegerField(choices=ownership, null=False)

    def __str__(self):
        return self.Desk_brand
    class Meta:
        verbose_name_plural="Desktops"

