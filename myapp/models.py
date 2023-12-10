from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    college = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    adhaar=models.FileField(upload_to='adhaar')