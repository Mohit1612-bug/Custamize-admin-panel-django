from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
# Create your models here.


class Person(models.Model):
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    courses = models.ManyToManyField("Course", blank=True)

    class Meta:
        ordering = ("last_name", "first_name")


    def __str__(self):
        return self.first_name

class Course(models.Model):
    name = models.CharField(max_length=255)
    year = models.IntegerField()

    class Meta:
        unique_together = ("name", "year", )
    def __str__(self):
        return self.name

class Grade(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    grade = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)])
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.grade}, {self.person}, {self.course}"
