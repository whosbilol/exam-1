from rest_framework import serializers
from .models import ProductModel
from category.models import CategoryModel
from django.contrib.auth.models import User

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')

class PoductSerializer(serializers.ModelSerializer):
    owner_full_name = serializers.SerializerMethodField()
    category_name = serializers.SerializerMethodField()

    class Meta:
        model = ProductModel
        exclude = ('category', 'owner')

    def get_owner_full_name(self, obj):
        return f'{obj.user.username}'

    def get_owner_full_name(self, obj):
        return f'{obj.category.name}'





