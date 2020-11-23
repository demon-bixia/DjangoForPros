from django.urls import path
from .views import BookListView, BookDetailView, SearchBookListView


urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('<uuid:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('search/', SearchBookListView.as_view(), name='book_search')   
]
