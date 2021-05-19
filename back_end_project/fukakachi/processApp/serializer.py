
# from .models import detailed_cost, projects,products_list, process,arise_cost_data
from users.models import NewUser
from rest_framework import serializers
from .models import data_set, analyzed_data
# # API Example: Project serializer
class DataSetSerializer(serializers.ModelSerializer):
    # product_name = serializers.CharField()
    # plant_name = serializers.CharField()
  
    class Meta:
        model = data_set
        fields = '__all__'



class UserSerializer(serializers.ModelSerializer):
    # product_name = serializers.CharField()
    # plant_name = serializers.CharField()
    class Meta:
        model = NewUser
        fields = '__all__'
# API Example: Project serializer

# API Example: Project serializer
class AnalyzedSerializer(serializers.ModelSerializer):
    # product_name = serializers.CharField()
    # plant_name = serializers.CharField()
    user = UserSerializer
    data_set = DataSetSerializer
    class Meta:
        model = analyzed_data
        fields = (
            'user',
            'id',
            'name',
            'description',
            'json',
            'csv_link',
            'data_set',
        )