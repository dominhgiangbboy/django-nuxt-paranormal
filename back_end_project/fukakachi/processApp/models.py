from django.db import models

# Data Set info
class data_set (models.Model):
    id = models.IntegerField(primary_key=True, auto_created = True)
    name = models.CharField(max_length=100, default='')
    description = models.TextField(default='')
    dataID = models.IntegerField(default=0)
    categoryID = models.IntegerField(default=1)
    typeID = models.IntegerField(default=1)
    userID = models.IntegerField(default=0)
    analyzedDataID = models.IntegerField(default=0)
    linkFolder = models.TextField(default='')
# Data
class data (models.Model):
    id = models.IntegerField(primary_key=True, auto_created = True)
    name = models.CharField(max_length=100, default='')
    download = models.TextField(default='')
# analyzed
class analyzed_data (models.Model):
    id = models.IntegerField(primary_key=True, auto_created = True)
    name = models.CharField(max_length=1000, default='')
    json = models.JSONField(encoder=None)
    csv_link = models.TextField(default='')