
from .models import detailed_cost, projects,products_list, process,arise_cost_data
from rest_framework import serializers


# API Example: Project serializer
class ProcessSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField()
    plant_name = serializers.CharField()
  
    class Meta:
        model = process
        fields = (
            'id',
            'name',
            'product_name',
            'project_id',
            'plant_name',
            'product_id',
            'plant_id',
            'process_type'
        )
# API Example: Project serializer
class ProcessDataSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField()
  
    class Meta:
        model = process
        fields = (
            'id',
            'name',
            'product_name',
            '一台当たりの付加価値額',
            '付加価値額',
            '実行予算金額',
            '日当りの目標付加価値額',
            '日当りの目標生産数量',
            '比率',
            '部材点数',
        )
# API Example: Project serializer
class ProcessDropdownSerializer(serializers.ModelSerializer):  
    class Meta:
        model = process
        fields = (
            'id',
            'name',
        )
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = projects
        fields = ('id',
        'name',
        '工事名',
        '契約金額',
        '材料費',
        '外注費',
        '付加価値額',
        )
class ProjectDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = projects
        fields = ('id',
        'name',
        '総付加価値額',
        '一日当り付加価値額収支',
        '年間必要固定費額',
        '月間必要固定費額',
        '一日当り必要固定費額',
        )
class AriseCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = arise_cost_data
        fields = "__all__"
# API Example: ProductSerializer
# add project_name field to model
class ProductSerializer(serializers.ModelSerializer):
    project_name = serializers.CharField()
    class Meta:
        model = products_list
        fields = ('id',
        'name',
        'project_id',
        'project_name')
        read_only_fields = (
            'project_name',
        )

# API Example: get targeted field
# add project_name field to model 
class ProductsDetailedSerializer(serializers.ModelSerializer):
    # project_name = serializers.CharField()
    class Meta:
        model = products_list
        fields = (
            'name',
            'id',
        )
    # API Example: get targeted field
# add project_name field to model 
class DetailedCostSerializer(serializers.ModelSerializer):
    # project_name = serializers.CharField()
    class Meta:
        model = detailed_cost
        fields = (
            'id',
            'name',
            'cost_id',
            'product_id',
            'total_cost_id',
            'date',
            '営業予算金額',
            '実行予算金額',
            '実行原価金額',
            '営業予算金額_calculated',
            '実行予算金額_calculated',
            '実行原価金額_calculated',
            '実行予算対原価差異_calculated',
            '構成比_calculated',
            'group_name',
            'project_id'
        )
    

    