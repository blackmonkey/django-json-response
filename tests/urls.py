from django.urls import path, include
from .views import (
  AuthorCreateView, AuthorDetailView, AuthorUpdateView, AuthorDeleteView, AuthorListView,
  PublisherCreateView, PublisherDetailView, PublisherUpdateView, PublisherDeleteView, PublisherListView,
  BookCreateView, BookDetailView, BookUpdateView, BookDeleteView, BookListView, ErrorView
)

urlpatterns = [
  path('accounts/', include('django.contrib.auth.urls')),

  path('authors/', AuthorListView.as_view(), name='authors'),
  path('authors/<int:pk>', AuthorDetailView.as_view(), name='author-details'),
  path("authors/create/", AuthorCreateView.as_view(), name="author-create"),
  path("authors/<int:pk>/update/", AuthorUpdateView.as_view(), name="author-update"),
  path("authors/<int:pk>/delete/", AuthorDeleteView.as_view(), name="author-delete"),

  path('publishers/', PublisherListView.as_view(), name='publishers'),
  path('publishers/<int:pk>', PublisherDetailView.as_view(), name='publisher-details'),
  path("publishers/create/", PublisherCreateView.as_view(), name="publisher-create"),
  path("publishers/<int:pk>/update/", PublisherUpdateView.as_view(), name="publisher-update"),
  path("publishers/<int:pk>/delete/", PublisherDeleteView.as_view(), name="publisher-delete"),

  path('books/', BookListView.as_view(), name='books'),
  path('books/<int:pk>', BookDetailView.as_view(), name='book-details'),
  path("books/create/", BookCreateView.as_view(), name="book-create"),
  path("books/<int:pk>/update/", BookUpdateView.as_view(), name="book-update"),
  path("books/<int:pk>/delete/", BookDeleteView.as_view(), name="book-delete"),

  path("error", ErrorView.as_view(), name="error"),
]
