from django.urls import path
from .views import *


urlpatterns = [
    path('book-list', Bookview.as_view(), name='booklist'),
    path('author-list', AuthorView.as_view(), name = 'authorlist'),
    path('book-details/<slug:isbn>',BookDetailsView.as_view(), name= "book_details")
]
