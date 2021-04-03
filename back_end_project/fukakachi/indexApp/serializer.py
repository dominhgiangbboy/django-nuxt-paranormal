
from .models import total_cost_list, production_plant_list, sub_process_list, process_list
from rest_framework import serializers


class ProcessListSerializer(serializers.ModelSerializer):
    工場 = serializers.CharField()
    class Meta:
        model = process_list
        fields =  ('id',
                    'name',
                    '大工程番号',
                    '工場',
                    "plant_id")

class SubProcessListSerializer(serializers.ModelSerializer):
    class Meta:
        model = sub_process_list
        fields =  "__all__"

class ProductPlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = production_plant_list
        fields =  "__all__"