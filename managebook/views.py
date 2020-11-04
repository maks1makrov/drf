from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.response import Response

from managebook.models import Book, Comment
from managebook.serialize import BookSerializer, CommentSerializer


class ListBook(ListAPIView):
    serializer_class = BookSerializer
#    queryset = Book.objects.all()
#     def get(self, request, id=None):
#         if id is None:
#             return Response(BookSerializer(Book.objects.all(), many=True).data)
#         return Response(BookSerializer(Book.objects.get(id=id)).data)
    def get_queryset(self):
        if self.kwargs.get('id'):
            return Book.objects.filter(id=self.kwargs.get('id'))
        return Book.objects.all()

class CreateBook(CreateAPIView):

    serializer_class = BookSerializer


class DestroyBook(DestroyAPIView):
    # def get_object(self):
    #     return Book.objects.get(id=self.kwargs['id'])

    lookup_field = 'id'
    def get_queryset(self):
        return Book.objects.all()

class UpdateBook(UpdateAPIView):
    serializer_class = BookSerializer
    def get_object(self):
        return Book.objects.get(id=self.kwargs['id'])

class ListComment(ListAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects