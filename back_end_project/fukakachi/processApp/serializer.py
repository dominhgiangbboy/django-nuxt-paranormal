
# from .models import detailed_cost, projects,products_list, process,arise_cost_data
from rest_framework import serializers
from .models import data_set
# # API Example: Project serializer
class DataSetSerializer(serializers.ModelSerializer):
    # product_name = serializers.CharField()
    # plant_name = serializers.CharField()
  
    class Meta:
        model = data_set
        fields = '__all__'
# API Example: Project serializer

    