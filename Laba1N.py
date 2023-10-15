import json

class LibraryException(Exception):
    def __init__(self,message):
        super().__init__(message)

class Book:
    def __init__(self, title, age, genre, author):
        if not isinstance(title, str):
            raise LibraryException("Title should be a string")
        if not isinstance(age, int) or age not in [0, 6, 12, 16, 18]:
            raise LibraryException("Invalid age category")
        if not isinstance(genre, str) or genre not in ["Drama", "Comedy", "Action", "Horror"]:
            raise LibraryException("Invalid genre")
        if not isinstance(author, str):
            raise LibraryException("Invalid author")
        self.__age = age
        self.__genre = genre
        self.__author = author
        self.__title = title#тайтл приватный
    def GetTitle(self):#ниже (то что тайтл)сделать то же с остальными переменными
        return self.__title
    def SetTitle(self,title):
        self.__title = title 
    def GetJSON(self):
        return {'title': self.__title, 'age': self.__age, 'genre': self.__genre, 'author': self.__author}
    def GetAge(self):
        return self.__age
    def SetAge(self,age):
        self.__age = age 
            
            
    def Gettype_Genre(self):#ниже (то что age )сделать то же с остальными переменными это уже я переписала
        return self.__genre
    def Settype_Genre(self,genre):
        self.__ = genre
             
    def GetAuthor(self):#ниже (то что тайтл)сделать то же с остальными переменными
        return self.__author
    def SetAuthor(self,author):
        self.__author = author
      
    

class Magazine:
    def __init__(self, title, age, type_mag,issue_num):
        if not isinstance(title, str):
            raise LibraryException("Title should be a string")
        if not isinstance(age, int) or age not in [0, 6, 12, 16, 18]:
            raise LibraryException("Invalid age category")
        if not isinstance(type_mag, str) or type_mag not in ["Sports", "Business", "Animals", "News"]:
            raise LibraryException("Invalid type_mag")
        if not isinstance(issue_num, int) or issue_num <= 0:
            raise LibraryException("Invalid number of issue_num")
        self.__age = age
        self.__type_mag = type_mag
        self.__issue_num = issue_num
        self.__title = title#тайтл приватный
    def GetTitle(self):#ниже (то что тайтл)сделать то же с остальными переменными
       return self.__title
    def SetTitle(self,title):
       self.__title = title 
    def GetJSON(self):
        return {'title': self.__title, 'age': self.__age, 'type_mag': self.__type_mag, 'issue_num': self.__issue_num}
    def GetAge(self):
        return self.__age
    def SetAge(self,age):
        self.__age = age 
            
            
    def GetType_mag(self):
        return self.__type_mag
    def SetType_mag(self,type_mag):
        self.__type_mag = type_mag
             
    def GetIssue_num(self):
        return self.__issue_num
    def SetIssue_num(self,issue_num):
        self.__issue_num = issue_num

class Library:
    def __init__(self):
        self.books = []
        self.magazines = []

    def import_data(self, json_file):
     with open(json_file, 'r') as file:
           data = json.load(file)
           self.books = [Book(n['title'], n['age'], n['genre'] ,n['author'])   for n in data['books']]
           self.magazines = [Magazine(k['title'], k['age'], k['type_mag'],k['issue_num']) for k in data['magazines']]

    def export_data(self, json_file):
        for n in self.books:
            print(n.GetJSON())
        data = {
            'books': [n.GetJSON() for n in self.books],
            'magazines': [n.GetJSON() for n in self.magazines]
        }
        with open(json_file, 'w') as file:
            json.dump(data, file, indent=4)

    def add_Book(self, title, age, genre, author):
        self.books.append(Book(title, age, genre, author))

    def add_Magazine(self, title, age, type_mag, issue_num):
        self.magazines.append(Magazine(title, age, type_mag, issue_num))

    def remove_Book(self, title):
        self.books = [n for n in self.books if n.title != title]

    def remove_Magazine(self, title):
        self.magazines = [k for k in self.magazines if k.title != title]


# Пример использования

Library = Library()


# Импорт данных из JSON файла

#try:
#   Library.import_data('data.json')
#except LibraryException as e:
#   print(f"Importing error: {str(e)}")
# Добавление книги/журнала
#Library.add_Book('The Shining', 18, "Horror",'Stephen King')
#Library.add_Magazine('Forbs', 18,"News",6)


# Удаление 
Library.remove_Magazine('Forbs')

# Экспорт данных в JSON файл
Library.export_data('data.json')
try:
    # Добавление Жупнала
    Library.add_Magazine('National Geographic',16,"Animals",2)
   
    # Добавление книги с некорректными атрибутами
    Library.add_Book('Harry Potter',16, "Action", "jj")  # Некорректный жанр
    
except LibraryException as e:
    print(f"Error: {str(e)}")

# Удаление книги
#Library.remove_Magazine('Game of Thrones')
try:
    Library.export_data('data.json')
except LibraryException as e:
    print(f"Export error: {str(e)}")
