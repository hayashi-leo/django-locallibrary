# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.



def catalog_home(request):
    # sort posts by published_date

    return render(request,
                  'catalog/test.html',
                  {})

from .models import Book, Author, BookInstance, Genre

def index(request):
    """
    View function for home page of site.
    """
    ### Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    ### Available books (status == 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count() # The 'all()' is implied by default.

    # Number of visits to this view, as counted in the session variable
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_books':num_books, 'num_instances':num_instances,
                 'num_instances_available':num_instances_available,
                 'num_authors':num_authors,
                 'num_visits': num_visits}, #num_visits appended
    )

from django.views import generic
class BookListView(generic.ListView):
    model = Book
    context_object_name = 'my_book_list' # your own name for the list as a template variable

    # queryset = Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war

    ### full path is  '/locallibrary/catalog/templates/catalog/book_list.html'
    template_name = 'catalog/book_list.html' # Specify your own template name/location
    paginate_by = 2   ### must also add a template pagination, see base_generic.html

class BookDetailView(generic.DetailView):
    model = Book
    context_object_name = 'my_book'
    template_name = 'catalog/book_detail.html'