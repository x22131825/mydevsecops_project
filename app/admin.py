from django.contrib import admin
from .models import Student #Now we are importing our class from model.py to register it in admin.py so that our stored Data should reflect on the admin webpage


# Register your models here.
admin.site.register(Student) #Here we have called our class function "Student" that we created in model.py.
