from django.shortcuts import render
from django.http import HttpResponse
from .models import Department
from .models import Doctor,Booking
from .forms import BookingForm
def index(request):
 
    person={
        'name':'john',
        'age':30,
        'place':'thrissur'
                }
    return render(request,"index.html",person)
def about(request):
    return render(request,"about.html",{'range':range(1,11)})
def show(request):
    number1={
       'num':[1,2,3,4,5,6,7]
             }
    return render(request,"show.html",number1)
def departments(request):
    dic_dept={
        'dept':Department.objects.all()
    }
    return render(request,"departments.html",dic_dept)
def doctor(request):
    dic_doc={
        'doc':Doctor.objects.all()
    }
    return render(request,"doctor.html",dic_doc)
def booking(request):
    if request.method=="POST":
        form=BookingForm(request.post)
        if form.is_valid():
            form.save()
    else:
        form=BookingForm()
    dic_form={
            'form':form
        }
    
    return render(request,"booking.html",dic_form)



