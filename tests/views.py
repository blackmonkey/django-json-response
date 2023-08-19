import base64

from django.views.generic import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django_json_response import JsonResponseMixin
from .models import Author, Book, Publisher


class AuthorListView(JsonResponseMixin, ListView):
  model = Author
  paginate_by = 5
  ordering = "pk"


class AuthorCreateView(JsonResponseMixin, CreateView):
  model = Author
  fields = ("name",)
  template_name = "author-create.html"
  success_url = reverse_lazy("authors")


class AuthorDetailView(JsonResponseMixin, DetailView):
  model = Author


class AuthorUpdateView(JsonResponseMixin, UpdateView):
  model = Author
  fields = ("name",)
  success_url = reverse_lazy("authors")


class AuthorDeleteView(JsonResponseMixin, DeleteView):
  model = Author
  success_url = reverse_lazy("authors")


class PublisherListView(JsonResponseMixin, ListView):
  model = Publisher
  paginate_by = 5
  ordering = "pk"


class PublisherCreateView(JsonResponseMixin, CreateView):
  model = Publisher
  fields = ("name",)
  template_name = "publisher-create.html"
  success_url = reverse_lazy("publishers")


class PublisherDetailView(JsonResponseMixin, DetailView):
  model = Publisher


class PublisherUpdateView(JsonResponseMixin, UpdateView):
  model = Publisher
  fields = ("name",)
  success_url = reverse_lazy("publishers")


class PublisherDeleteView(JsonResponseMixin, DeleteView):
  model = Publisher
  success_url = reverse_lazy("publishers")

##Book Views
class BookListView(JsonResponseMixin, ListView):
  model = Book
  paginate_by = 5
  ordering = "pk"


class BookCreateView(JsonResponseMixin, CreateView):
  model = Book
  fields = ("author","publisher","title",)
  template_name = "book-create.html"
  success_url = reverse_lazy("books")


class BookDetailView(JsonResponseMixin, DetailView):
  model = Book


class BookUpdateView(JsonResponseMixin, UpdateView):
  model = Book
  fields = ("author","publisher","title",)
  success_url = reverse_lazy("books")


class BookDeleteView(JsonResponseMixin, DeleteView):
  model = Book
  success_url = reverse_lazy("books")


class ErrorView(JsonResponseMixin, DetailView):
  def get_object(self):
    raise ValueError('Something went wrong.')

# TODO:
# 1. Test internal errors
# 2. Test Login success and failure
# 3. Test failure of above views
