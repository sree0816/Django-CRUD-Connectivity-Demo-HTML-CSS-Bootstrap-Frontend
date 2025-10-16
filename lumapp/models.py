from django.db import models

# Create your models here.
class Course_table(models.Model):
    course_name=models.CharField(max_length=20,blank=True,null=True)
    duration=models.IntegerField(blank=True,null=True)
    fees=models.CharField(max_length=20,null=True,blank=True)
    description=models.CharField(max_length=20,null=True,blank=True)
    trainer_name=models.CharField(max_length=20,null=True,blank=True)

class Employee_table(models.Model):
    name=models.CharField(max_length=20,blank=True,null=True)
    dob=models.DateField(blank=True,null=True)
    age=models.IntegerField(blank=True,null=True)
    qualification=models.CharField(max_length=20,blank=True,null=True)
    contact=models.CharField(max_length=20,blank=True,null=True)
    email=models.CharField(max_length=20,blank=True,null=True)
    designation=models.CharField(max_length=20,blank=True,null=True)
    salary=models.CharField(max_length=20,blank=True,null=True)