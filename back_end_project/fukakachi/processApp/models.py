from django.db import models
from users.models import NewUser
from indexApp.models import data_category
# Data Set info
class data_set (models.Model):
    id = models.AutoField(primary_key=True, auto_created = True)
    name = models.CharField(max_length=100, default='')
    description = models.TextField(default='')
    type_id = models.IntegerField(default=1)
    # Foreign keys
    category = models.ForeignKey(
        data_category
        , default=1
        , on_delete=models.CASCADE
        )
    linkFolder = models.TextField(default='')
# analyzed
class analyzed_data (models.Model):
    id = models.AutoField(primary_key=True, auto_created = True)
    name = models.CharField(max_length=1000, default='')
    description = models.TextField(default='')
    json = models.JSONField(encoder=None)
    csv_link = models.TextField(default='')
    #### Foreign keys
    data_set = models.ForeignKey(
        data_set
        , default=1
        , on_delete=models.CASCADE
        )
    user = models.ForeignKey(
        NewUser
        , default=1
        , on_delete=models.CASCADE
        )
    