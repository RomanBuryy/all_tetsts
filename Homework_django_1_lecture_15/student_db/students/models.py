from django.db import models
# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length=30, blank=False)
    second_name = models.CharField(max_length=30, blank=False)
    birthday = models.DateField(null=True, blank=True)
    photo = models.ImageField(blank=True, null=True)
    notes = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.first_name} {self.second_name}"
