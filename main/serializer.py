from rest_framework import serializers
from. models import *



class BookCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCategory
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class BookDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookDetail
        fields = "__all__"