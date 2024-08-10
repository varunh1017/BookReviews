from django.shortcuts import render
from rest_framework import generics
from .models import Book, Review
from .serializers import BookSerializer, ReviewSerializer
import pandas as pd 
from django.http import JsonResponse

# Handles listing all reviews and creating new books
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Manages retrieval, updating, and deletion of a specific review
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Handles listing all reviews and creating new reviews
class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

# Manages retrieval, updating, and deletion of a specific review
class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

# Computes and returns average ratings and review counts for each book
def book_statistics_view(request):
    reviews = Review.objects.all().values()
    reviews_df = pd.DataFrame(reviews)
    
    avg_ratings = reviews_df.groupby('book_id')['rating'].mean().reset_index()
    review_counts = reviews_df.groupby('book_id').size().reset_index(name='review_count')
    
    book_stats = pd.merge(avg_ratings, review_counts, on='book_id')
    book_stats_dict = book_stats.to_dict(orient='records')
    
    return JsonResponse(book_stats_dict, safe=False)

