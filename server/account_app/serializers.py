from .models import VisitorModel
from rest_framework import serializers

class VisitorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitorModel
        fields = '__all__'