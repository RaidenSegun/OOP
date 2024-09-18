class Person: 
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married
    
    def introduce_myself(self):
        print(f'Меня зовут {self.fullname}, мне {self.age}-лет, и я {self.is_married}')

class Teacher(Person):
    def __init__(self, fullname, age, is_married, experience):
        super().__init__(fullname, age, is_married)
        self.experience = experience
        self.salary = 0

    def calculate_salary(self):
        base_salary = 30000
        bonus = (self.experience // 3) * 3000
        self.salary = base_salary + bonus
        return self.salary

    def introduce_myself(self):
        base_intro = super().introduce_myself()
        return f"Опыт работы: {self.experience} лет, Зарплата: {self.salary} сом"


teacher = Teacher("Арзымамат уулу Баяман", 31, 'не женат', 10)
teacher.calculate_salary()
print(teacher.introduce_myself())
