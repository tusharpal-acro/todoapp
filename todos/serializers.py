from rest_framework import serializers
from .models import Category, Todo


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        def get_fields(self):
            fields = super(CategorySerializer, self).get_fields()
            fields['subcategories'] = CategorySerializer(many=True)
            return fields



class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"
