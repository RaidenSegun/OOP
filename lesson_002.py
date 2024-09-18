""" Объектно ориентированное програмирование """

""" Наследование и множественное наследование """

# class Game: 
#     def __init__(self, game_name, graphics, game_year, company):
#         self.game_name = game_name
#         self.graphics = graphics
#         self.game_year = game_year
#         self.company = company
    
#     def info(self):
#         print(f'Название игры - {self.game_name}, макимальная графика - {self.graphics}, дата релиза - {self.game_year}, создатели - {self.company}')

# game = Game('CsGO', 'FULL HD 4K', 2013, 'Valve')
# # game.info()

# class Roblox(Game):
#     def __init__(self, game_name, graphics, game_year, company, multiplayer):
#         Game.__init__(self, game_name, graphics, game_year, company)
#         self.multiplayer = multiplayer
#         self.name = 'player'
#         self.gender = 'gender'
#         self.skin = 'skin'
#         self.hp = 1000000000000000

#     # def info(self):
#     #     print(f'Название игры - {self.game_name}, макимальная графика - {self.graphics}, дата релиза - {self.game_year}, создатели - {self.company}, мультиплеер - {self.multiplayer}')
#     def info_player(self):
#         print(f'Игрок - {self.name}, Пол - {self.gender}, Облик - {self.skin}, здоровье - {self.hp}')
#         print("========================================================================\nROBLOX - запустился и готов к игре!")

#     def edit_player(self):
#         name = input("Введите имя игрока: ")
#         gender = input("Введите пол игрока: ")
#         skin = input("Введите облик игрока: ")
#         self.name = name
#         self.gender = gender
#         self.skin = skin




# roblox = Roblox("Roblox", "ULTRA", "2006", "Roblax Corporation", "Да")
# # roblox.info()
# # roblox.edit_player()
# # roblox.info_player()


# class Snake(Roblox):
#     def __init__(self, name, gender, skin):
#         self.name = name
#         self.gender = gender
#         self.skin = skin
#         self.hp = 1000000000000000000000000000000000000

# snake = Snake("Бека", "Мужчина", "Platinum")
# snake.info()
# snake.info_player()



class Animal: 
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f'{self.name} - ест')

    def sleep(self):
        print(f'{self.name} - спит')

koza = Animal('Коза')
koza.eat()
koza.sleep()

class Walker(Animal):
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(f'{self.name} - ходит')
    
koza = Walker("Коза")
koza.walk()

class Swimmer(Walker):
    def __init__(self, name):
        super().__init__(name)

    def swim(self):
        print(f'{self.name} - плавает')

koza = Swimmer("Коза")
koza.swim()


class Flyer(Swimmer):
    def __init__(self, name):
        super().__init__(name)

    def fly(self):
        print(f'{self.name} - летает')

koza = Flyer("Коза")
koza.fly()


class Penguin(Animal):
    def __init__(self, name):
        super().__init__(name)

    def describe(self):
        print('describe')

penguin = Penguin('Пин')
penguin.describe()

