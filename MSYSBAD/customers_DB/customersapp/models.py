from django.db import models
from django.utils import timezone
# Create your models here.

class Customer(models.Model):
    Name = models.CharField(max_length = 300)
    address = models.CharField(max_length = 300)
    contact_number = models.CharField(max_length=12)
    emailaddress = models.CharField(max_length = 300)
    
    def getName(self):
        return self.Name
    
    def __str__(self):
        return str(self.pk) + ": " + str(self.Name) + "," + str(self.address) + ", " + str(self.contact_number) + ", " + str(self.emailaddress) 

#class Order(models.Model):
  #  Customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
  #  OrderNum = models.Charfield(max_length = 6, unique=True)
  #  IssueDate = models.DateTimeField(blank=True, null=True)
  #  Description = models.CharField(max_length = 300)


class Account(models.Model):
    username = models.CharField(max_length=250, unique = True)
    password = models.CharField(max_length=250)
    # objects = models.Manager()

    def getUsername(self):
        return f"{self.username}"

    def getPassword(self):
        return f"{self.password}"

    def __str__(self):
        return f"{self.pk}: {self.username}"