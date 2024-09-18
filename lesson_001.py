# """ Объектно ориентированное програмирование """
# # full_name = 'Аслан'                                      # - Змейиный регистр

# # FullName = 'Жибек'                                       # - Жерблюжий регистр 

# class Car:                                                 # - шаблон или же чертеж
#     def __init__(self, marka, model, color):               # __init__ (Магический метод) 
#         #Атрибуты объекта
#         self.marka = marka                                 # - self (Ссылка на текущий объект)
#         self.model = model 
#         self.color = color
#         self.bak = 10
#         self.is_start = False
        
#     def info(self):
#         print(f"Марка машины - {self.marka}, модель - {self.model}, Цвет - {self.color}")
    
#     def start(self):
#         if self.bak > 0:
#             self.is_start = True
#             print(f"Машина {self.marka} - {self.model} заведена")
#         else:
#             print(f"Машина {self.marka} - {self.model} нет топлива")

#     def stop(self):
#         self.is_start = False
#         print(f"Машина {self.marka} - {self.model} заглушено")

#     def drive(self, city):
#         if self.is_start == True:
#             print(f"Машина {self.marka} - {self.model} едет в {city}")
#         else:
#             print(f"Машина {self.marka} - {self.model} не заведена")
        

# bmw = Car('BMW', 'M5 F90', 'Black')
# bmw.info()
# bmw.start() 
# # bmw.stop()       
# bmw.drive("Дубай")    



class Book:                                                
    def __init__(self, book_name, avtor, year):              
        self.book_name = book_name                              
        self.avtor = avtor
        self.year = year
    def info(self):
        print(f"Название книги - {self.book_name}, имя автора - {self.avtor}, в каком году написано - {self.year}")

voina_i_mir = Book("Война и мир", "Лев Николаевич Толстой", "1856-год")
voina_i_mir.info()

