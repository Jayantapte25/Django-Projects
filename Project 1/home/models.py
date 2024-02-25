from django.db import models    

# Create your models here.
class contact(models.Model):
    name = models.CharField(max_length=122)
    email= models.CharField(max_length=122)
    phone= models.CharField(max_length=12)
    desc= models.TextField()
    date= models.DateField()

    def __str__(self):
        return self.name #this is done to show the name of the person in the admin panel instead of contact object(1)

