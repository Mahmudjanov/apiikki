from django.urls import path
from. views import *

urlpatterns = [
    path('get-bookcategory/', get_bookcategory_view),
    path('get-book/', get_book_view),
    path('get-author/', get_author_view),
    path('get-bookdetail/', get_bookdetail_view),
    path('get-search/', get_search_view),
]