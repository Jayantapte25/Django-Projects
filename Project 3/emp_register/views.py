from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee

def employee_list(request): #So in this function we are fetching all the data from the database & displaying it in the employee_list.html file
    context = {'employee_list': Employee.objects.all()} 
    return render(request, "emp_register/employee_list.html", context)

#So we access the form in 2 ways 
#1. First time to add in the elements
#2. Second time to update the elements

#So we take Id=0, it means that if Id=0 then we are adding the elements & if Id!=0 then we are updating the elements
#also if we get POST request then we are adding the elements & if we get GET request then we are updating the elements
def employee_form(request, id=0):
    if request.method == "GET": 
        if id == 0:
            form = EmployeeForm() #we are just creating a new form object
        else:
            #so this is the case when we are updating the elements
            employee = Employee.objects.get(pk=id) 
            form = EmployeeForm(instance=employee)         
        return render(request, "emp_register/employee_form.html", {'form': form}) 
    else:
        #when we are in the update section we select update option and we are redirected to the forms
        #When we enter the changes and submit the form it is updated as the new entry in the form and not changing or updating the same columnwhich we wanted to update
        #That is why here we are checking if ID=0 or not
        if id == 0:
            form = EmployeeForm(request.POST) 
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST, instance=employee) 

        if form.is_valid(): #in this we are checking if the form is valid or not
            form.save() #if the form is valid then we are saving the form
        return redirect('/employee/list')      #if the form is not valid then we are redirecting the user to the employee/list url 

#so in the above function we are checking if the request is GET or POST. If it is GET then we are checking if the id is 0 or not. If it is 0 then we are creating a new form object & passing it to the employee_form.html file. If it is not 0 then we are fetching the employee object from the database & passing it to the employee_form.html file. If the request is POST then we are checking if the id is 0 or not. If it is 0 then we are creating a new form object & passing the request.POST data to it. If it is not 0 then we are fetching the employee object from the database & passing it to the form object & then passing the request.POST data to it. Then we are checking if the form is valid or not. If it is valid then we are saving the form object & redirecting the user to the employee/list url.
def employee_delete(request, id):
    employee = Employee.objects.get(pk=id) #we are taking the id of the element we want to delete & then deleting it
    #unique id is present in the database for every element
    employee.delete()
    return redirect('/employee/list')