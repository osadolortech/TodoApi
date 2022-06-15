from dataclasses import fields
from rest_framework import serializers
from .models import Todolist

class Todoserielizers(serializers.ModelSerializer):
    class Meta:
        model = Todolist
        fields =(
            'id', 'title','completed'
        )