from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=40)
    address=models.CharField(max_length=100)
    age=models.IntegerField()
    mobile=models.IntegerField(max_length=10)   
    image=models.FileField(upload_to="myimages")
