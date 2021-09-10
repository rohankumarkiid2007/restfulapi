from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Employees

class employeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields=['firstname','lastname']
        fields = '__all__'