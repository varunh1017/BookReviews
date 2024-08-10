from django.urls import path
from .views import BookListCreateView, BookDetailView, ReviewListCreateView, ReviewDetailView, book_statistics_view

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('reviews/', ReviewListCreateView.as_view(), name='review-list-create'),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
    path('book-stats/', book_statistics_view, name='book-stats')
]
