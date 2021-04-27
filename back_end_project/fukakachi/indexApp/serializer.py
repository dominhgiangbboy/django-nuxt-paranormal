
from .models import data_category
from rest_framework import serializers




class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = data_category
        fields =  "__all__"

