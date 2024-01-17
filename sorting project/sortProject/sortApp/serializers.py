from rest_framework import serializers
from . models import *

class productserializer(serializers.ModelSerializer):
    class Meta:
        model=product
        fields='__all__'
        
class feedbackserializer(serializers.ModelSerializer):
    class Meta:
        model=feedback
        fields='__all__'      
        
