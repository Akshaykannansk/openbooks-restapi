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

class AuthorView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = Authorserializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['$name',]


class BookDetailsView(APIView):
    # def get_object(self, name):
    #     print ('nameeeeeeeee',name)
    #     try:
    #         return Books.objects.get(title=name)
    #     except Books.DoesNotExist:
    #         raise Http404

    def get(self, request, format=None):
        name = request.GET.get("name", None)
        try:
            if name:
                print('nameeeeeeeeeeeeeeee', name)
                books = Books.objects.get(title=name)
                serializer = Bookserializer(books)
                return Response(serializer.data)
        except Books.DoesNotExist:
             raise Http404

    # def put(self, request, format=None):
    #     Books = self.get_object(name)
    #     serializer = Bookserializer(Books, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, format=None):
    #     Books = self.get_object(name)
    #     Books.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)