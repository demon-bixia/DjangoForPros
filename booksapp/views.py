from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Book

class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'

class BookDetailView(DetailView):
    model = Book
    context_object_name = "book"
    template_name="books/book_detail.html"