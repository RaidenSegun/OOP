# class Fruits:                                                
#     def __init__(self, name, color, weight):              
#         self.name = name                              
#         self.color = color
#         self.weight = weight
#     def info(self):
#         print(f"Название фрукта - {self.name}, цвет фрукта - {self.color}, масса фрукта в граммах - {self.weight}")

# yabloko = Fruits("Яблоко", "Красный", "180")
# yabloko.info()




# class Fruits:                                                
#     def __init__(self, name, color, weight):              
#         self.name = name                              
#         self.color = color
#         self.weight = weight
#     def info(self):
#         print(f"Название фрукта - {self.name}, цвет фрукта - {self.color}, масса фрукта в граммах - {self.weight}")

# banan = Fruits("Банан", "Жёлтый", "150")
# banan.info()




# class Fruits:                                                
#     def __init__(self, name, color, weight):              
#         self.name = name                              
#         self.color = color
#         self.weight = weight
#     def info(self):
#         print(f"Название фрукта - {self.name}, цвет фрукта - {self.color}, масса фрукта в килограммах - {self.weight}")

# arbuz = Fruits("Арбуз", "Зеленый", "6")
# arbuz.info()




class Book:                                                
    def __init__(self, title, author, pages):              
        self.title = title                              
        self.author = author
        self.pages = int(pages)

    def info(self):
        print(f"Название книги - {self.title}, имя автора - {self.author}, сколько страниц в данной книге - {self.pages}")


    def check_pages(self):
        if self.pages < 100:
            print("Это книга является тонкой")
        elif 100 <= self.pages <= 300:
            print("Это книга является средней")
        else:
            print("Это книга является толстой")


kniga = Book("Опасная жизнь Джейд Йео", "Зен Чо", "87")
kniga_2 = Book("Старик и море", "Эрнест Хемингуэй",  "107")
kniga_3 = Book("Война и мир", "Лев Николаевич Толстой", "1300")
kniga.info()
kniga.check_pages()
kniga_2.check_pages()
kniga_3.check_pages()
