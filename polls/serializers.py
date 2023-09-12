from rest_framework import serializers
from .models import authorModel,bookModel

class authorSerializer(serializers.ModelSerializer):
    class Meta:
        model=authorModel
        fields=('__all__')

class bookSerializer(serializers.ModelSerializer):
    class Meta:
        model=bookModel
        fields=('__all__')