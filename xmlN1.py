import xml.etree.ElementTree as ET

class LibraryException(Exception):
    def __init__(self,message):
        super().__init__(message)

class Magazine:
    def __init__(self, title, age, type_mag,issue_num):
        if not isinstance(title, str):
            raise LibraryException("Title should be a string")
        if not isinstance(age, int) or age not in [0, 6, 12, 16, 18]:
            raise LibraryException("Invalid age category")
        if not isinstance(type_mag, str) :
            raise LibraryException("Type should be a string")
        if not isinstance(issue_num, int) or issue_num <= 0:
            raise LibraryException("Invalid duration")
        self.title = title
        self.age = age
        self.type_mag = type_mag
        self.issue_num = issue_num

class Book:
    def __init__(self, title, genre, author,age):
        if not isinstance(title, str):
          raise LibraryException("Title should be a string")
        if not isinstance(genre, str) or genre not in ["Fantasy", "Non-fiction", "Action", "Horror"]:
          raise LibraryException("Invalid genre")
        if not isinstance(author, str):
         raise LibraryException("Author should be a string")
        if not isinstance(age, int) or age not in [0, 6, 12, 16, 18]:
          raise LibraryException("Invalid age category")
        self.title = title
        self.genre = genre
        self.author = author
        self.age = age

class Library:
    def __init__(self):
        self.magazines = []
        self.books = []

    def import_data(self, xml_file):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        
        self.magazines = []
        self.books = []


        for magazine_elem in root.findall('magazines/magazine'):
         title = magazine_elem.find('title').text
         age = int(magazine_elem.find('age').text)
         type_mag = magazine_elem.find('type_mag').text
         issue_num = int(magazine_elem.find('issue_num').text)
         self.magazines.append(Magazine(title, age, type_mag, issue_num))

         for book_elem in root.findall('books/book'):
          title = book_elem.find('title').text
          genre = book_elem.find('genre').text
          author = book_elem.find('author').text
          age = int(book_elem.find('age').text)
          self.books.append(Book(title, genre, author, age))

    def export_data(self, xml_file):
        root = ET.Element("library")

        magazines_elem = ET.SubElement(root, "magazines")
        for magazine in self.magazines:
            magazine_elem = ET.SubElement(magazines_elem, "magazine")
            ET.SubElement(magazine_elem, "title").text = magazine.title
            ET.SubElement(magazine_elem, "age").text = str(magazine.age)
            ET.SubElement(magazine_elem, "type_mag").text = magazine.type_mag
            ET.SubElement(magazine_elem, "issue_num").text = str(magazine.issue_num)

        books_elem = ET.SubElement(root, "books")
        for book in self.books:
            book_elem = ET.SubElement(books_elem, "book")
            ET.SubElement(book_elem, "title").text = book.title
            ET.SubElement(book_elem, "genre").text = book.genre
            ET.SubElement(book_elem, "author").text = book.author
            ET.SubElement(book_elem, "age").text = str(book.age)

        tree = ET.ElementTree(root)
        tree.write(xml_file, encoding="utf-8", xml_declaration=True)

    def add_magazine(self, title, age, type_mag, issue_num):
        self.magazines.append(Magazine(title, age,type_mag, issue_num))

    def add_book(self, title, genre, author, age):
        self.books.append(Book(title, genre, author, age))

    def remove_magazine(self, title):
        self.magazines = [m for m in self.magazines if m.title != title]

    def remove_book(self, title):
        self.books = [s for s in self.books if s.title != title]


# Пример использования

Library = Library()

# Импорт данных из JSON файла

try:
   Library.import_data('data.json')
except LibraryException as e:
   print(f"Importing error: {str(e)}")

try:
    # Добавление 
    Library.add_magazine('Forbs', 12, "Bussines", 11)
    
    # Добавление  
    Library.add_book('The Shining', 'Horror', 'Stiven king', 18)
    
except LibraryException as e:
    print(f"Error: {str(e)}")

# Удаление сериала
#Library.remove_book('Game of Thrones')
try:
    Library.export_data('data.xml')
    
except LibraryException as e:
    print(f"Export error: {str(e)}")
