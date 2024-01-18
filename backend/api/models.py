from django.db import models

# Create your models here.
class Company(models.Model):
    name=models.CharField(max_length=50)
    website=models.URLField(max_length=100)
    foundation=models.PositiveIntegerField()

class Tournament(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    # Otros campos relacionados con el torneo

    def __str__(self):
        return self.name