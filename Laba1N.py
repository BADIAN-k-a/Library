import json

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

    def import_data(self, json_file):
        with open(json_file, 'r') as file:
            data = json.load(file)
            self.magazines = [Magazine(m['title'], m['age'], m['type'] ,m['issue number'])   for m in data['magazines']]
            self.books = [Book(s['title'], s['genre'], s['author'],s['age']) for s in data['books']]

    def export_data(self, json_file):
        data = {
            'magazines': [{'title': m.title, 'age': m.age, 'genre': m.type_mag, 'duration': m.issue_num} for m in self.magazines],
            'books': [{'title': s.title, 'genre': s.genre, 'author': s.author, 'age': s.age} for s in self.books]
        }
        with open(json_file, 'w') as file:
            json.dump(data, file, indent=4)

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
    # Добавление фильма
    Library.add_magazine('Forbs', 12, "Bussines", 11)
    
    # Добавление сериала с некорректными атрибутами
    Library.add_book('The Shining', 'Horror', 'Stiven king', 18)  # Некорректный жанр
    
except LibraryException as e:
    print(f"Error: {str(e)}")

# Удаление сериала
#Library.remove_serial('Game of Thrones')
try:
    Library.export_data('data.json')
except LibraryException as e:
    print(f"Export error: {str(e)}")


