# school_infrastructure/models.py

from django.db import models

class Building(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name

class Facility(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

