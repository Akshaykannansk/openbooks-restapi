from rest_framework import serializers
from .models import Books, Author

class Bookserializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(many=True, read_only = False)
    class Meta:
        model = Books
        fields = ['id', 'title', 'isbn', 'author']
    

class Authorserializer(serializers.ModelSerializer):
    books = Bookserializer(many= True,read_only= False)
    class Meta:
        model = Author 
        fields = ['name','books']