from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from rest_framework.utils import json

from managebook.models import Book
from managebook.serialize import BookSerializer


class TestBook(APITestCase):
    def test_create(self):
        url = reverse("create")
        data = {
            "title": "title text",
            "text": "text ttt"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        count_book = Book.objects.all().count()
        self.assertEqual(count_book, 1)

    def test_delete(self):
        book = Book.objects.create(title="test t", text="tes;odjf")
        url = reverse("delete", kwargs={"id": book.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        count_book = Book.objects.all().count()
        self.assertEqual(count_book, 0)

    def test_list(self):
        book1 = Book(title="test t", text="tes;odjf")
        book2 = Book(title="test t2", text="tes;odjf2")
        Book.objects.bulk_create([book1, book2])
        url = reverse("list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()[0]['title'], "test t")
        self.assertEqual(response.json()[1]['title'], "test t2")

    # def test_update(self):
    #     book = Book.objects.create(title="test t", text="tes;odjf")
    #     data = {
    #         "title": "title text",
    #         "text": "text ttt"
    #     }
    #     url = reverse("update", kwargs={id: book.id})
    #     response = self.client.put(url, json.dumps(data))
    #     self.assertEqual(response.status_code, )

    def test_update(self):
        book = Book.objects.create(title="test t", text="tes;odjf")
        data = {
            "title": "title text",
            "text": "text ttt"
        }
        url = reverse("update", kwargs={"id": book.id})
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)