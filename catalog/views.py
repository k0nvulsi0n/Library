from django.shortcuts import render
from .models import Book, Author, Genre
from django.views import generic


# Create your views here.
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()
    context = {
        'num_books': num_books,
        'num_authors': num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'catalog/index.html', context=context)

class BookListView(generic.ListView):
    model = Book
    contecontext_object_name = 'book_list'
    def get_queryset(self):
        return Book.objects.all()
    template_name = 'catalog/books.html'

# BACKUP: in case I get tired of learning CBVs:
# def books(request):
#     books = Book.objects.all()
#     context = {'books': books}
#     return render (request,'catalog/books.html' ,context=context)