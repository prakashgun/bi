from django.db import models


class Location:
    name = models.CharField(max_length=255)


class Company:
    name = models.CharField(max_length=255)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)


class Product:
    name = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    material_cost = models.FloatField(default=0)
    indirect_cost = models.FloatField(default=0)
    labor_cost = models.FloatField(default=0)
    revenue = models.FloatField(default=0)
    defects_percentage = models.FloatField(default=0)


class Item:
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
