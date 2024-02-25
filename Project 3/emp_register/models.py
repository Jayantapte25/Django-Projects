from django.db import models
#in this wholde code is there is nothing new, we are only doing the same thing which we have done in the previous project

#now the value returned by position table will be the title of the position table
class position(models.Model):  
    title = models.CharField(max_length=50)  

#self is used to return the title of the position table
    def __str__(self): #__str__ is a method which is used to return the string representation of the object
        return self.title

class Employee(models.Model):
    fullname = models.CharField(max_length=100) #here we are just creating a text field with max length of 100 in form
    emp_code = models.CharField(max_length=3)
    mobile = models.CharField(max_length=15)
    position = models.ForeignKey(position, on_delete=models.CASCADE) #here we are creating a foreign key to position table and on delete we are cascading it
    #cascade meaning is that if we delete the position table then the employee table will also be deleted
