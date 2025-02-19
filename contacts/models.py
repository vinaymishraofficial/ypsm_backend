from django.db import models

# Create your models here.
class Enquiry(models.Model):
    fullName = models.CharField(max_length=255)
    fatherName = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    gender = models.CharField(max_length=255)
    dob = models.CharField(max_length=255)
    address = models.TextField()
    pcbpercentage = models.FloatField()
    neetScore = models.FloatField()
    course = models.CharField(max_length=255)
    
    def __str__(self):
        return f'{self.fullName}/{self.fatherName}'


class Contact(models.Model):
    fullName = models.CharField(max_length=255)
    fatherName = models.CharField(max_length=255)
    email = models.EmailField()
    contactNo = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.fullName