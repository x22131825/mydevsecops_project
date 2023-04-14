from django.shortcuts import render,redirect
from .models import Student #we are importing the class from model.py that we created, to call this function for storing the student Database
from django.contrib import messages
# Create your views here.

#Create function for index.html page
def index(request):
    data=Student.objects.all()
    print(data)
    context={"data":data}
    return render(request,"index.html",context)


# Create function to insertData.

def insertData(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        print(name,email,age,gender) 
        query=Student(name=name,email=email,age=age,gender=gender) #We called here our class function "Student" from model.py.
        query.save() #This is to save the particular Data that we are entering to be stored in DB
        messages.info(request,"Data Inserted Successfully")
        return redirect("/")
    
    return render(request,"index.html")

#Create function to Update the Student Details

def updateData(request,id):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        age=request.POST['age']
        gender=request.POST['gender']
        
        edit=Student.objects.get(id=id)
        edit.name=name
        edit.email=email
        edit.age=age
        edit.gender=gender
        edit.save()
        messages.warning(request,"Data Updated Successfully")
        
        return redirect("/")
    
    d=Student.objects.get(id=id)
    context={"d":d}
    return render(request,"edit.html",context)


#Create function to Delete the Student Data

def deleteData(request,id):
    d=Student.objects.get(id=id)
    d.delete()
    messages.error(request,"Data Deleted Successfully")
    return redirect("/")