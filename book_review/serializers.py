from rest_framework import serializers
from .models import Book, Review

# Serializes all fields of the Book model for API representation
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        
# Serializes all fields of the Review model for API representation
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
