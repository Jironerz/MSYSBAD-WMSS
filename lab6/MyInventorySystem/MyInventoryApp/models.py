from django.db import models
from django.utils import timezone 

# Create your models here.
class Supplier(models.Model):
    name = models.CharField(max_length = 300)
    city = models.CharField(max_length = 300)
    country = models.CharField(max_length = 300)
    created_at = models.DateTimeField(blank=True, null=True)

    def getName(self):
        return self.name

    def formatDate(self):
        format_date = self.created_at.strftime("%m/%d/%Y, %I:%M %p")
        return format_date

    def __str__(self):
        return str(self.pk) + ": " + str(self.name) + "," + "- " + str(self.city) + ", " + str(self.country) + " " + "created at: " + str(self.formatDate()) 


class WaterBottle(models.Model):
    SKU = models.CharField(max_length = 300, unique=True)
    brand = models.CharField(max_length = 300)
    cost = models.DecimalField(max_digits=100000, decimal_places=2)
    size = models.CharField(max_length = 300)
    mouth_size = models.CharField(max_length = 300)
    color = models.CharField(max_length = 300)
    supplier = models.ForeignKey(Supplier, on_delete = models.CASCADE)
    current_quantity = models.IntegerField()

    def __str__(self):
        return str(self.pk) + ": " + str(self.SKU) + ": " + str(self.brand) + ", " + str(self.mouth_size) + ", " + str(self.size) + ", " + str(self.color) + ", " + "supplied by " + str(self.supplier.getName()) + ", " + str(self.cost) + ": " + str(self.current_quantity)
        

class Account(models.Model):
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=250)

    def getUsername(self):
        return f"{self.username}"

    def getPassword(self):
        return f"{self.password}"

    def __str__(self):
        return f"{self.pk}: {self.username}"

