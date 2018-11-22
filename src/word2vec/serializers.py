from rest_framework import serializers

from .models import Word2Vec


class Word2VecSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word2Vec
        fields = '__all__'
