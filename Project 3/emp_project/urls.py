from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), #this is the default url for admin
    path('employee/', include('emp_register.urls', namespace='emp_register')), #this is the url for employee
    path('', include('emp_register.urls', namespace='emp_register')), #this is the url for employee
]
