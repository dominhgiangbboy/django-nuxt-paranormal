from django.db import models

# Bảng dự án

class projects (models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, default='')
    工事名 = models.CharField(max_length=100, default='')
    契約金額 = models.CharField(max_length=100, default='')
    材料費 = models.CharField(max_length=100, default='')
    外注費 = models.CharField(max_length=100, default='')
    付加価値額 = models.IntegerField(default=0)
    総付加価値額 = models.IntegerField(default=0)
    一日当り付加価値額収支 = models.IntegerField(default=0)
    年間必要固定費額 = models.IntegerField(default=0)
    月間必要固定費額 = models.IntegerField(default=0)
    一日当り必要固定費額 = models.IntegerField(default=0)
    実行予算計画後合計 = models.IntegerField(default=0)
    def __str__(self):
        return self.id
# proccess data
class process(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, default='')
    product_id = models.IntegerField(default=1)
    plant_id =  models.IntegerField(default=1)
    project_id = models.IntegerField(default=1)
    process_type = models.IntegerField(default=1)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    is_calculate =  models.BooleanField(default=True)
    実行予算金額 =  models.IntegerField(default=0)
    比率 =  models.FloatField(default=0.0)
    付加価値額 =  models.IntegerField(default=0)
    部材点数 =  models.IntegerField(default=0)
    一台当たりの付加価値額 =  models.IntegerField(default=0)
    日当りの目標生産数量 =  models.IntegerField(default=0)
    日当りの目標付加価値額 =  models.IntegerField(default=0)
    
class sub_process(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, default='')
    product_id = models.IntegerField(default=1)
    plant_id =  models.IntegerField(default=1)
    project_id = models.IntegerField(default=1)
    process_type = models.IntegerField(default=1)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    実行予算金額 =  models.FloatField(default=0.0)
    比率 =  models.FloatField(default=0.0)
    付加価値額 =  models.FloatField(default=0.0)
    部材点数 =  models.FloatField(default=0.0)
    一台当たりの付加価値額 =  models.FloatField(default=0.0)
    日当りの目標生産数量 =  models.FloatField(default=0.0)
    日当りの目標付加価値額 =  models.FloatField(default=0.0)

# Công trình
class products_list(models.Model):
    # Basic informations
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, default='')
    date = models.DateTimeField(auto_now_add=True, blank=True)
    project_id = models.IntegerField(default=1)
    # Other informations
# sai lech
class arise_cost_data(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, default='')
    date = models.DateTimeField(auto_now_add=True, blank=True)
    project_id = models.IntegerField(default=1)
    value = models.IntegerField(default=1)
# detailed cost
class detailed_cost(models.Model):
    # Basic informations
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, default='')
    group_name = models.CharField(max_length=100, default='')
    cost_id = models.IntegerField(default=1)
    product_id = models.IntegerField(default=1)
    project_id = models.IntegerField(default=1)
    total_cost_id =  models.IntegerField(default=1)
    date = models.DateTimeField(auto_now_add=True, blank=True)

    # value
    営業予算金額 = models.FloatField(default=0.0)
    実行予算金額 = models.FloatField(default=0.0)
    実行原価金額 = models.FloatField(default=0.0)
    # calculated value
    営業予算金額_calculated = models.FloatField(default=0.0)
    実行予算金額_calculated = models.FloatField(default=0.0)
    実行原価金額_calculated = models.FloatField(default=0.0)
    実行予算対原価差異_calculated = models.FloatField(default=0.0)
    構成比_calculated = models.FloatField(default=0.0)

class total_cost(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, default='')
    product_id = models.IntegerField(default=1)
    total_cost_id =  models.IntegerField(default=1)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    #insert value
    設計費予測額 = models.FloatField(default=0.0)
    設計費予測損失額 = models.FloatField(default=0.0)
    溶接長 = models.FloatField(default=0.0)
    塗装面積 = models.FloatField(default=0.0)
    #calculated value
    営業予算金額 = models.FloatField(default=0.0)
    実行予算金額 = models.FloatField(default=0.0)
    実施金額 = models.FloatField(default=0.0)
    営業予算対実行予算 = models.FloatField(default=0.0)
    営業予算対実施金額差額合計 = models.FloatField(default=0.0)
    実行予算対実施金額差額合計 = models.FloatField(default=0.0)
    設計費予測単価 = models.FloatField(default=0.0)
    設計費損失予測単価 = models.FloatField(default=0.0)
    仕口ブラケット加工費の柱加工費への影響単価 = models.FloatField(default=0.0)
    柱加工費予算額 = models.FloatField(default=0.0)
    柱加工費実施額 = models.FloatField(default=0.0)
    柱加工費予算単価 = models.FloatField(default=0.0)
    柱加工費実施単価 = models.FloatField(default=0.0)
    形鋼一次加工費予測単価 = models.FloatField(default=0.0)
    大梁加工費予算額 = models.FloatField(default=0.0)
    大梁加工費実施額 = models.FloatField(default=0.0)
    大梁加工費予算単価 = models.FloatField(default=0.0)
    大梁加工費実施単価 = models.FloatField(default=0.0)
    営業予算対実施金額差額総合計 = models.FloatField(default=0.0)
    実行予算対実施金額差額合計 = models.FloatField(default=0.0)

    