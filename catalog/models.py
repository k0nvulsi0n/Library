from django.db import models
from django.urls import reverse
import uuid

# Create your models here.
class Genre(models.Model):
    """Model representing a book genre."""
    name = models.CharField(max_length=200, help_text='Enter a book genre (e.g. Science Fiction)')

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)
    bio = models.TextField(max_length=2000, null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the URL to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'

class Book(models.Model):
    title = models.CharField(max_length=200, help_text='Enter the title')
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=2000, help_text='Enter a brief description of the book')
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')
    # BOOK_STATUS = (
    #     ('n', 'Not interested'),
    #     ('i', 'Interested'),
    #     ('o', 'Own'),
    #     ('r', 'Read'),
    # )
    # status = models.CharField(
    #     max_length=1,
    #     choices=BOOK_STATUS,
    #     blank=True,
    #     default='n',
    #     help_text='Have you read this book?',
    # )
    # if status == 'r':
    #     date_read = models.DateField()
    # else:
    #     date_read = models.DateField(null=True, blank=True)
    
    class Meta:
        ordering = ['title', 'author']
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])
    
    def display_genre(self):
        return ', '.join(genre.name for genre in self.genre.all()[:3])

    display_genre.short_description = 'Genre'
