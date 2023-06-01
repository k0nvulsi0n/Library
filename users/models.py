from django.db import models
from catalog.models import Book, Genre, Author
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField
# Create your models here.


class User(AbstractUser):
    prof_pic = models.ImageField(default='default.jpg', upload_to='profile_pics')
    country = CountryField()
    user_bio = models.TextField(max_length=1000, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    fav_books = models.ManyToManyField(Book, help_text="Select your favourite books")
    fav_genres = models.ManyToManyField(Genre, help_text="Select your favourite genres")
    fav_authors = models.ManyToManyField(Author, help_text="Select your favourite authors")