
# models.py
from django.db import models

class State(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class PreviousSchool(models.Model):
    previous_school = models.CharField(max_length=100)
    year_of_start = models.DateField()
    year_of_end = models.DateField()

    def __str__(self):
        return self.previous_school

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True)
    address = models.TextField()
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    pincode = models.CharField(max_length=6)
    subjects = models.ManyToManyField(Subject)
    previous_educational_details = models.ManyToManyField(PreviousSchool,null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
