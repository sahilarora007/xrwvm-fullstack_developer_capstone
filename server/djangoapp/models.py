# Uncomment the following imports before adding the Model code

from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime

# Create your models here.

# Car Make model
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


# Car Model model
class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)  # Many-to-One relationship
    name = models.CharField(max_length=100)

    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        # Add more types if needed
    ]

    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')
    year = models.IntegerField(
        default=datetime.datetime.now().year,
        validators=[
            MinValueValidator(2015),
            MaxValueValidator(datetime.datetime.now().year)
        ]
    )
    dealer_id = models.IntegerField()  # Refers to a Cloudant dealer

    def __str__(self):
        return f"{self.car_make.name} {self.name} ({self.year})"

