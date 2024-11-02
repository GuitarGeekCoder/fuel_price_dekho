from django.db import models

# Create your models here.
class Fuel_price(models.Model):
    city_name = models.CharField(max_length=255)
    petrol_price=models.CharField(max_length=255)
    diesel_price=models.CharField(max_length=255)

    def __str__(self):
        return f"{self.city_name} - {self.petrol_price}  - {self.diesel_price}"