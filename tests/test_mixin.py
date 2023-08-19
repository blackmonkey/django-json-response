import json

from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.test import TestCase, Client
from django.urls import reverse
from .models import Author, Publisher, Book


class JsonResponseMixinTestCase(TestCase):
  def assert_response(self, response, status_code, content, content_type='application/json'):
    self.assertEqual(response.status_code, status_code)
    self.assertEqual(response.headers['content-type'], content_type)
    self.assertEqual(json.loads(response.content.decode()), content)


class ErrorTestCase(JsonResponseMixinTestCase):
  def test_error_response(self):
    response = self.client.get(reverse('error'), follow=True)
    self.assert_response(response, 500, {'error': 'Something went wrong.'})


class AuthorCRUDTestCase(JsonResponseMixinTestCase):
  def setUp(self):
    super().setUp()
    self.author = Author.objects.create(name='John Doe')

  def tearDown(self):
    super().tearDown()
    Author.objects.all().delete()

  def test_create_author(self):
    response = self.client.post(reverse('author-create'), {'name': 'Jane Smith'}, follow=True)
    self.assertEqual(Author.objects.count(), 2)
    self.assertRedirects(response, reverse('authors'))

  def test_get_author(self):
    response = self.client.get(reverse('author-details', kwargs={'pk': 1}))
    self.assert_response(response, 200, {'object': {'model': 'tests.author', 'name': 'John Doe', 'pk': 1}})

  def test_update_author(self):
    response = self.client.post(reverse('author-update', args=[self.author.pk]), {'name': 'John Doe Jr.'})
    self.author.refresh_from_db()
    self.assertEqual(self.author.name, 'John Doe Jr.')
    self.assertRedirects(response, reverse('authors'))

  def test_delete_author(self):
    response = self.client.post(reverse('author-delete', args=[self.author.pk]))
    self.assertFalse(Author.objects.filter(pk=self.author.pk).exists())
    self.assertRedirects(response, reverse('authors'))


class PublisherCRUDTestCase(JsonResponseMixinTestCase):
  def setUp(self):
    super().setUp()
    self.publisher = Publisher.objects.create(name='ABC Publisher')

  def tearDown(self):
    super().tearDown()
    Publisher.objects.all().delete()

  def test_create_publisher(self):
    response = self.client.post(reverse('publisher-create'), {'name': 'XYZ Publisher'})
    self.assertEqual(Publisher.objects.count(), 2)
    self.assertRedirects(response, reverse('publishers'))

  def test_get_publisher(self):
    response = self.client.get(reverse('publisher-details', kwargs={'pk': 1}))
    self.assert_response(response, 200, {'object': {'model': 'tests.publisher', 'name': 'ABC Publisher', 'pk': 1}})

  def test_update_publisher(self):
    response = self.client.post(reverse('publisher-update', args=[self.publisher.pk]), {'name': 'ABC Publisher Inc.'})
    self.publisher.refresh_from_db()
    self.assertEqual(self.publisher.name, 'ABC Publisher Inc.')
    self.assertRedirects(response, reverse('publishers'))

  def test_delete_publisher(self):
    response = self.client.post(reverse('publisher-delete', args=[self.publisher.pk]))
    self.assertFalse(Publisher.objects.filter(pk=self.publisher.pk).exists())
    self.assertRedirects(response, reverse('publishers'))


class BookCRUDTestCase(JsonResponseMixinTestCase):
  def setUp(self):
    super().setUp()
    self.author = Author.objects.create(name='John Doe')
    self.publisher = Publisher.objects.create(name='ABC Publisher')
    self.book = Book.objects.create(title='Book 1', author=self.author, publisher=self.publisher)

  def tearDown(self):
    super().tearDown()
    Book.objects.all().delete()

  def test_create_book(self):
    response = self.client.post(reverse('book-create'), {'title': 'Book 2', 'author': self.author.pk, 'publisher': self.publisher.pk})
    self.assertEqual(Book.objects.count(), 2)
    self.assertRedirects(response, reverse('books'))

  def test_get_book(self):
    response = self.client.get(reverse('book-details', kwargs={'pk': 1}))
    self.assert_response(response, 200, {'object': {'model': 'tests.book', 'title': 'Book 1', 'pk': 1, 'author': 1, 'publisher': 1}})

  def test_update_book(self):
    response = self.client.post(reverse('book-update', args=[self.book.pk]), {'title': 'Updated Book', 'author': self.author.pk, 'publisher': self.publisher.pk})
    self.book.refresh_from_db()
    self.assertEqual(self.book.title, 'Updated Book')
    self.assertRedirects(response, reverse('books'))

  def test_delete_book(self):
    response = self.client.post(reverse('book-delete', args=[self.book.pk]))
    self.assertFalse(Book.objects.filter(pk=self.book.pk).exists())
    self.assertRedirects(response, reverse('books'))


class PaginationTestCase(TestCase):
  def setUp(self):
    super().setUp()

    # create 11 authors
    for i in range(1, 12):
      Author.objects.create(name=f'Author {i}')

  def tearDown(self):
    super().tearDown()
    Author.objects.all().delete()

  def test_author_list_pagination(self):
    response = self.client.get(reverse('authors'))
    self.assertEqual(response.status_code, 200)

    data = json.loads(response.content.decode())
    self.assertEqual(len(data['object_list']), 5)
    self.assertEqual(len(data['page_obj']['object_list']), 5)
    self.assertEqual(data['object_list'], data['page_obj']['object_list'])

    response = self.client.get(reverse('authors') + '?page=2')
    self.assertEqual(response.status_code, 200)

    data = json.loads(response.content.decode())
    self.assertEqual(len(data['object_list']), 5)
    self.assertEqual(len(data['page_obj']['object_list']), 5)
    self.assertEqual(data['object_list'], data['page_obj']['object_list'])

    response = self.client.get(reverse('authors') + '?page=3')
    self.assertEqual(response.status_code, 200)

    data = json.loads(response.content.decode())
    self.assertEqual(len(data['object_list']), 1)
    self.assertEqual(len(data['page_obj']['object_list']), 1)
    self.assertEqual(data['object_list'], data['page_obj']['object_list'])
