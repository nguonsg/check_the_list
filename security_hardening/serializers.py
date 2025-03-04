from rest_framework import serializers
from .models import SecurityCheck

class SecurityCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecurityCheck
        fields = '__all__'

