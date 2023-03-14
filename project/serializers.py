from rest_framework import serializers
from .models import Category, Project

# class ProjectSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Project
#         fields = ('id', 'name', 'description', 'price', 'client', 'is_active', 'is_completed')
#         read_only_fields = ('id', 'client', 'is_active', 'is_completed')






class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        exclude = ('created_by',)

    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        return super().create(validated_data)


class ProjectDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class ProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        exclude = ('created_by', 'updated_at')
