import xml.etree.ElementTree as ET

class Book:
    def __init__(self, title, author_name, author_birthplace, year, genre, book_id):
        self.title = title
        self.author_name = author_name
        self.author_birthplace = author_birthplace
        self.year = year
        self.genre = genre
        self.book_id = book_id

    def __str__(self):
        return f"ID: {self.book_id}, Title: {self.title}, Author: {self.author_name}, Birthplace: {self.author_birthplace}, Year: {self.year}, Genre: {self.genre}"

# Распарсим XML-файл и создадим объекты класса Book
tree = ET.parse('venv/library.xml')
root = tree.getroot()

books = []
for book in root.findall('book'):
    title = book.find('title').text
    author = book.find('author')
    author_name = author.find('name').text
    author_birthplace = author.find('birthplace').text
    year = int(book.find('year').text)
    genre = book.find('genre').text
    book_id = book.attrib['id']
    books.append(Book(title, author_name, author_birthplace, year, genre, book_id))

# Выведем информацию о книгах
for book in books:
    print(book.author_name)