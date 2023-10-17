from rest_framework import serializers
from .models import Books, Author

class Bookserializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(many=True)
    class Meta:
        model = Books
        fields = ['id', 'title', 'isbn', 'author']
    

class Authorserializer(serializers.ModelSerializer):
    books = Bookserializer(many= True,)
    class Meta:
        model = Author 
        fields = ['name','books']