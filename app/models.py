from django.db import models

# Create your models here.
# We are creating a class to store the student Data from this Class function

class Student(models.Model):
    name=models.CharField(max_length=25, blank=False, null=False) #Name Could be 25 Char long and Field should not be Blank.
    email=models.EmailField()
    age=models.IntegerField()
    gender=models.CharField(max_length=25, blank=False, null=False)
    
    def __str__(self) :
        return self.name