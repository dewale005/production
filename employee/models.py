from django.db import models

# Create your models here.
class Employee(models.Model):
    First_Name = models.CharField(max_length=20)
    Last_Name = models.CharField(max_length=20)
    Email = models.EmailField()
    Phone_Number = models.BigIntegerField()
    Address = models.CharField(max_length=200)

    def __str__(self):
        return self.First_Name