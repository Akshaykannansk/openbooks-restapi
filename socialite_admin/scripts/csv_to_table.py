from books.models import Books, Author
import csv
from datetime import datetime
def run():
    with open('books/books.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        for row in reader:
            print("title:",row[1])
            authorlist = row[2].split("/")
            print("authorsssssss", authorlist)
            for oneauthor in authorlist:
                author, _ = Author.objects.get_or_create(name = oneauthor)
                title = row[1]
                average_rating = row[3]
                isbn = row[4]
                isbn13 = row[5]
                lan_code = row[6]
                pages = row[7]
                pub_date = row[10]
                pub_date = datetime.strptime(pub_date, '%m/%d/%Y').date()
                publisher = row[11]
                book,_ = Books.objects.get_or_create(title= title,average_rating = average_rating,isbn=isbn, isbn13=isbn13, language_code=lan_code,num_pages = pages,publication_date=pub_date,publisher=publisher)
                book.author.add(author)
                print ('authorrrrrrrrrrrrrrrrr', oneauthor)
                print ('rowwwwwwwwwwwwwwwwwwwwwwwwwww', row[0])


        
