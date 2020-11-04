from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

from managebook.models import Book, Comment


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]

class BookSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Book
        fields = "__all__"


class CommentSerializer(ModelSerializer):
    book = BookSerializer()
    user = UserSerializer()
    class Meta:
        model = Comment
        fields = "__all__"
