from django.db import models

# Create your models here.

# Database example 
class data_category (models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200, default='')