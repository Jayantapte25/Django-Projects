from django import forms
from .models import Employee 

#here we are creating a new form & django has inbuild forms
#we create a new class & inherit the forms.ModelForm class
#after that we specify the model which we are using in this form
#class meta is used to specify which model we are using in this form

class EmployeeForm(forms.ModelForm):  
    
    class Meta:  #this is used to specify which model we are using in this form
        model = Employee  #So we are taking all the attributes of forms from the models & taking input from the user.
        fields = ('fullname','mobile','emp_code','position') #here we are specifying which fields we want to show in the form
        labels = {
            'fullname':'Full Name', #here we are just changing the labels of the fields
            'emp_code':'EMP. Code'
        }
    
    def __init__(self, *args, **kwargs): #this line is the basic syntax for the constructor in python & __init__ is always called automatically when we create an object of a class.
        super(EmployeeForm, self).__init__(*args, **kwargs) 
        self.fields['position'].empty_label = "Select" #this is used to make the position field as a dropdown list.
        self.fields['emp_code'].required = False #this is used to make the emp_code field optional & not mandatory.


    