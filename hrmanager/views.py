import os

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from employee.models import Employee
from .forms import EmployeeForm


# Create your views here.
def index(request):
    employess = Employee.objects.all().order_by('-created_at')

    context = {
        'title': 'Home',
        'employees': employess
    }
    return render(request, 'hrmanager/home.html', context=context)


def create_employee_record(request):
    context = {}
    form = EmployeeForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        form = EmployeeForm()
    else:
        form = EmployeeForm(request.POST, request.FILES)

    context['title'] = 'Create Employee'
    context['form'] = form
    return render(request, 'hrmanager/create_employee.html', context=context)


def update_employee_record(request, id):

    context = {}
    existing_employee_record = Employee.objects.get(pk=id)
    form = EmployeeForm(request.POST, request.FILES, instance=existing_employee_record)
    if request.method == "POST":
        if form.is_valid():
            try:
                image_path = existing_employee_record.image.path
                if os.path.exists(image_path):
                    os.remove(image_path)
            except:
                pass
            form.save()
            form = EmployeeForm()
        else:
            form = EmployeeForm(request.POST, request.FILES)

    context['title'] = 'Create Employee'
    context['form'] = form
    return render(request, 'hrmanager/create_employee.html', context=context)

def delete_employee_record(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('home')
