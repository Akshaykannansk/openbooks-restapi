from django.shortcuts import render
from .models import Author,Books
from .serializers import Authorserializer, Bookserializer
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters
# Create your views here.
class Bookview(ListAPIView):
    queryset = Books.objects.all()
    serializer_class = Bookserializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['$title',]


class AuthorView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = Authorserializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['$name',]


class BookDetailsView(APIView):
    def get_object(self, isbn):
        
        try:
            if len(isbn) == 13:
                return Books.objects.get(isbn13=isbn)
            if len(isbn) == 10:
                return Books.objects.get(isbn=isbn)
        except Books.DoesNotExist:
            raise Http404

    def get(self, request,isbn, format=None):
        books = self.get_object(isbn)
        serializer = Bookserializer(books)
        return Response(serializer.data)
    

    def put(self, request, isbn, format=None):
        Books = self.get_object(isbn)
        serializer = Bookserializer(Books, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, isbn, format=None):
        Books = self.get_object(isbn)
        Books.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
