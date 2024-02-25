from django.urls import path
from . import views

app_name = 'emp_register' #this is used to specify the app name

urlpatterns = [
    path('', views.employee_form, name='employee_insert'), 
    #So here we are using name=employee_insert so that we can call this in the employee list.Html file through href
    #The above strip is not necessary we can directly pass the URL in the href
    path('<int:id>/', views.employee_form, name='employee_update'), 
    #So we are sending a perticular id in the URL & we get which column or row to update using this id in the URL.
    #name='employee_update' is used to update the employee

    path('delete/<int:id>/', views.employee_delete, name='employee_delete'), 
    #Here we are adding delete slash because we have already used <int:id> once above.
    path('list/', views.employee_list, name='employee_list'), #we are just redirecting to list in views if we get list/ in URL.
]

# Django Architecture:
# models are used to create tables in database & they are used to create objects in database.
# views are used to create functions which are used to perform CRUD operations.
# urls are used to create URLs for the views.
# templates are used to create HTML pages.
