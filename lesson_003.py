""" Объектно ориентированное програмирование """
""" Инкапсуляция """

class PublicExample:
    def __init__(self, value):
        self.value = value       # Публичный атрибут

    def info(self):
        print(self.value)        #  Публичный метод

# public = PublicExample(42)
# # public.info()
# print (public.info())     # Вызов публичного метода
# print (public.value)     # Публичный атрибут


#Защишенный

class ProtectedExample:
    def __init__(self, value):
        self.value = value       # Защищенный атрибут

    def info(self):
        return self.value        #  Защищенный метод

# protected = ProtectedExample(50)
# print(protected.info())     # Это работает, но противоречит принцыпам инкапсуляций
# print(protected.value)     # Можно получить значение напрямую, но это не рекомендуется


#Приватный

class PrivateExample:
    def __init__(self, value):
        self.__value = value   # Приватный атрибут
    
    def __info(self):
        return self.__value    # Приватный метод
    
    def access_private(self):
        return self.__info()     # Публичный метод, где мы получаем доступ к приватному атрибуту
    
private = PrivateExample(300)

    # Прямой вызов приватного метода, вызовет ошибку
# print(private.__info())

    # Прямой вызов приватного атрибута, вызовет ошибку
# print(private.__value)

    # Доступ через публичный метод
# print(private.access_private())

    # Доступ к приватному атрибуту через (name mangling)
print(private._PrivateExample__value)




class MobileLegends:
    def __init__(self, person, rang, item, history):
        self.person = person        # Публичный атрибут
        self.rang = rang            # Публичный атрибут
        self._item = item           # Защищенный атрибут
        self.__history = history    # Приватный атрибут

    def player_info(self):
        print(f'Персонаж - {self.person}, Ранг - {self.rang}, История - {self.__history},')

    def _item_player(self):
        bag = input('Введите предметы:\n ')
        self._item = bag 

    def __history_player(self):
        print({self.__history})

    def access__history_player(self):
        return self.__history_player()
    
mobileLegends = MobileLegends('HAHA', 'Легенда', 'Облик .....', '-6 звезд')
print(mobileLegends._item_player())
mobileLegends.player_info()
print(mobileLegends.acces())



