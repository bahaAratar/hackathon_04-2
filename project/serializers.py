from rest_framework import serializers
from .models import Project , Category


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'price', 'client', 'is_active', 'is_completed')
        read_only_fields = ('id', 'client', 'is_active', 'is_completed')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'