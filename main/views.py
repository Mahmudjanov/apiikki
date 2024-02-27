from rest_framework.decorators import api_view
from rest_framework.response import Response
from. serializer import *



@api_view(['GET'])
def get_bookcategory_view(request):
    bookcategory = BookCategory.objects.all()
    serialized_data = BookCategorySerializer(bookcategory, many=True).data
    return Response(serialized_data)


@api_view(['GET'])
def get_book_view(request):
    book = Book.objects.all()
    serialized_data = BookSerializer(book, many=True).data
    return Response(serialized_data)


@api_view(['GET'])
def get_author_view(request):
    author = Author.objects.all()
    serialized_data = AuthorSerializer(author, many=True).data
    return Response(serialized_data)


@api_view(['GET'])
def get_bookdetail_view(request):
    bookdetail = BookDetail.objects.all()
    serialized_data = BookDetailSerializer(bookdetail, many=True).data
    return Response(serialized_data)


@api_view(['GET'])
def get_search_view(request):
    q = request.GET.get('q')
    author = Author.objects.filter(name__icontains=q)
    serialized_data = AuthorSerializer(author, many=True).data
    return Response(serialized_data)