from django.contrib import admin
from django.urls import path
from home import views

#makemigrations - create changes and store in a file
#migrate - apply the pending changes created by makemigrations

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='home'),
    path('about', views.about,name='about'),
    path('services', views.services,name='services'),
    path('contact', views.submit_contact,name='contact'),
]