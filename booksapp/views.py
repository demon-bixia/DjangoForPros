from typing import List
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Book
from django.db.models import Q

class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'

class BookDetailView(DetailView):
    model = Book
    context_object_name = "book"
    template_name="books/book_detail.html"

class SearchBookListView(ListView):
    model = Book
    context_object_name = "books"
    template_name="books/book_search.html"

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))
