from django.db import models

# Create your models here.

# Database example 
class roles_list (models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200, default='')
    access = models.CharField(max_length=100, default='')
# Danh mục phân xưởng
class production_plant_list(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200, default='')
    class Meta:
        managed = True
        db_table = 'indexApp_production_plant_list'
# Danh mục chi phí tổng
class total_cost_list(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200, default='')
# Danh mục chi phí 
class sub_process_list(models.Model):
    id = models.IntegerField(primary_key=True)
    程番号 = models.CharField(max_length=200, default='')
    name = models.CharField(max_length=200, default='')
    id_process = models.IntegerField(default=0)
    default = models.BooleanField(default=True)
    is_calculate =  models.BooleanField(default=True)
#Danh mục Tổng hợp
class process_list(models.Model):
    id = models.IntegerField(primary_key=True)
    plant_id = models.IntegerField(default=1)
    name = models.CharField(max_length=200, default='')
    大工程番号 = models.CharField(max_length=200, default='')
    
# DM dự toán thực hiện