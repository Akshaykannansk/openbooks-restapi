from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'author'

class Books(models.Model):
    title = models.CharField(max_length= 255)
    average_rating = models.FloatField()
    isbn = models.CharField(max_length=255)
    author = models.ManyToManyField(Author, related_name= 'books')
    isbn13 = models.CharField(max_length=255)
    language_code = models.CharField(max_length= 10)
    num_pages = models.SmallIntegerField(default=0)
    publication_date = models.DateField(blank=True, null=True)
    publisher = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    class Meta:
        db_table = 'books'

