from django.db import models

# Create your models here.
class Destination(models.Model):
    name=models.CharField(max_length=30)
    img=models.ImageField(upload_to='pics')
    desc=models.CharField(max_length=500)
    price=models.CharField(max_length=30)
    offer=models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Subscribe(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=100)



    def __str__(self):
        return self.name



class Contacts(models.Model):
    email=models.CharField(max_length=30)
    subject=models.CharField(max_length=30)
    message=models.TextField()

    def __str__(self):
        return self.email