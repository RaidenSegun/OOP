class Computer:
    def __init__(self, cpu, memory):
        self.__cpu =  cpu
        self.__memory = memory 
    def __make_computations(self):
        add = self.__cpu + self.__memory
        sub = self.__cpu - self.__memory
        mult = self.__cpu * self.__memory
        div = self.__cpu / self.__memory if self.__memory != 0 else "Ошибка: деление на 0"
        return f"Сложение: {add}, Вычитание: {sub}, Умножение: {mult}, Деление: {div}"
    
    def acces(self):
        return self.__make_computations()
    
    def get_cpu(self):
        return self.__cpu
    
    def get_memory(self):
        return self.__memory
    
    def info(self):
        computations = self.__make_computations()
        return f"Процессор: {self.__cpu}, Память: {self.__memory}"
    
    
class Laptop(Computer):
    def __init__(self, cpu, memory, memory_card):
        super().__init__(cpu, memory)
        self.__memory_card = memory_card

    def get_memory_card(self):
        return self.__memory_card
    
    def info(self):
        baze_info = super().info()
        return f"{baze_info}, Карта памяти: {self.__memory_card}"

computer = Computer(4.5, 24)
laptop = Laptop(3.5, 16, 512)

print("Computer Info:")
print(computer.info())
print("Laptop Info:")
print(laptop.info())

print("  Методы:")
print(F"Процессор компьютера: {computer.get_cpu()}")
print(F"Оперативная память компьютера: {computer.get_memory()}")
print(F"Процессор ноутбука: {laptop.get_cpu()}")
print(F"Оперативная память ноутбука: {laptop.get_memory()}")
print(F"Карта памяти ноутбука: {laptop.get_memory_card()}")
print(computer.acces())
