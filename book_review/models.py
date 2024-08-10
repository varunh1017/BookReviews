from django.db import models

# Represents a book with title, author, genre, and publication date
class Book(models.Model): 
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    publication_date = models.DateField() 

    def __str__(self): 
        return self.title

# Represents a review for a book, including content, rating, and reviewer details
class Review(models.Model): 
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    review_content = models.TextField()
    rating = models.IntegerField()
    reviewer_name = models.CharField(max_length=255)
    review_date = models.DateField(auto_now_add=True)

    def __str__(self): 
        return f"{self.reviewer_name}'s review of {self.book.title}"