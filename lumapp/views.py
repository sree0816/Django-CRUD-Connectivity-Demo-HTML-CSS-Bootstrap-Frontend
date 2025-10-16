from django.shortcuts import render,redirect
from lumapp.models import Course_table,Employee_table


# Create your views here.

def add_course(request):
    return render(request,'add_course.html')
def save_course(request):
    if request.method=='POST':
        a=request.POST.get('course_name')
        b=request.POST.get('duration')
        c=request.POST.get('fees')
        d=request.POST.get('desc')
        e=request.POST.get('trainer_name')
        obj=Course_table(course_name=a,duration=b,fees=c,description=d,trainer_name=e)
        obj.save()
    return redirect(add_course)
def display_course(request):
    data=Course_table.objects.all()
    return render(request,'display_course.html',{'data':data})
def edit_course(request,c_id):
    data=Course_table.objects.get(id=c_id)
    return render(request,'edit_course.html',{'data':data})
def update_course(request,c_id):
    if request.method=='POST':
        a=request.POST.get('course_name')
        b=request.POST.get('duration')
        c=request.POST.get('fees')
        d=request.POST.get('desc')
        e=request.POST.get('trainer_name')
        Course_table.objects.filter(id=c_id).update(course_name=a,duration=b,fees=c,description=d,trainer_name=e)
    return redirect(display_course)
def delete_course(request,c_id):
    data=Course_table.objects.filter(id=c_id)
    data.delete()
    return redirect(display_course)

def add_employee(request):
    return render(request,'add_employee.html')

def save_employee(request):
    if request.method=='POST':
        a=request.POST.get('name')
        b=request.POST.get('dob')
        c=request.POST.get('age')
        d=request.POST.get('qualification')
        e=request.POST.get('contact')
        f=request.POST.get('email')
        g=request.POST.get('designation')
        h=request.POST.get('salary')
        obj=Employee_table(name=a,dob=b,age=c,qualification=d,contact=e,email=f,designation=g,salary=h)
        obj.save()
    return redirect(add_employee)
def display_employee(request):
    data=Employee_table.objects.all()
    return render(request,'display_employee.html',{'data':data})
def edit_employee(request,e_id):
    data=Employee_table.objects.get(id=e_id)
    return render(request,'edit_employee.html',{'data':data})
def update_employee(request,e_id):
    if request.method == 'POST':
        a = request.POST.get('name')
        b = request.POST.get('dob')
        c = request.POST.get('age')
        d = request.POST.get('qualification')
        e = request.POST.get('contact')
        f = request.POST.get('email')
        g = request.POST.get('designation')
        h = request.POST.get('salary')
        Employee_table.objects.filter(id=e_id).update(name=a,dob=b,age=c,qualification=d,contact=e,email=f,designation=g,salary=h)
    return redirect(display_employee)
def delete_employee(request,e_id):
    data=Employee_table.objects.filter(id=e_id)
    data.delete()
    return redirect(display_employee)

def add_student(request):
    return render(request,'add_student.html')