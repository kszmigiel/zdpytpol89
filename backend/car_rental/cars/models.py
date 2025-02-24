from django.db import models

# Create your models here

class Brand(models.Model):
    name = models.CharField(max_length=100)
    date_of_founding = models.DateField()

    def __str__(self):
        return self.name


class Car(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.CharField(max_length=100)
    VIN = models.CharField(max_length=100, unique=True)
    mileage = models.IntegerField()

    def __str__(self):
        return self.brand.name + " " + self.model


class Rental(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    price_per_day = models.IntegerField()
