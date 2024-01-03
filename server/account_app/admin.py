from django.contrib import admin
from .models import VisitorModel

@admin.register(VisitorModel)
class VisitorModelSerializer(admin.ModelAdmin):
    class Meta:
        model = VisitorModel
        fields = '__all__'