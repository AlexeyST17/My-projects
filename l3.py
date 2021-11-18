class Prime:
    """Основной класс от которого будут наследоваться остальные
    (имеет конструктор с полями имени(модели) и возраста)"""
    def __init__(self, name='', age=''):
        self.name = name
        self.age = age


class Animals(Prime):
    """Высшая позиция иерархии - животное.
    (Имеют методы: питаться, рожать, думать)"""
    def eat(self):
        print(self.name, "eст")

    def think(self):
        print(self.name, "думает")

    def reproduction(self):
        print(self.name, "воспроизводит")


class Medusa(Animals):
    """Медуза - животное, которое умеет жалить"""
    def sting(self):
        print("Я медуза, я жалю!")


class Paws(Animals):
    """Животное, имеющее лапы может что-то взять"""
    def take(self):
        print(self.name, "взял")


class Puppy(Paws):
    """Щенок умеет гавкать, но не умеет рожать"""
    def reproduction(self):
        print("Я еще слишком маленький, чтобы рожать, потому что я щенок!")

    def woof(self):
        print("Гав, гав, гав!")


class Dog(Puppy):
    """Умеет тоже самое, что и щенок, но уже может рожать"""
    def reproduction(self):
        print(f"Я пёс по имени {self.name} и я умею рожать.")


class Flying(Prime):
    """Что-то, что умеет летать"""
    def fly(self):
        print(self.name, " летит")


class FlyingSquirrel(Paws, Flying):
    """Блека-летяга - животное, которое имеет лапы и умеет летать"""


class Eagle(Paws, Flying):
    """Орел - животное, которое имеет лапы и умеет летать"""


class Reasonable(Prime):
    """Что-то, что способно осуществлять какие-то логические операции"""
    def addition(self, num1, num2):
        print("Сумма двух чисел =", num1 + num2)


class Human(Paws, Reasonable):
    """Человек умеет тоже самое, что и животное, но умеет логически мыслить. Ещё он умеет говорить"""
    def talk(self):
        print("Hello! My name's %s. I'm %s years old." % (self.name, self.age))


class Blowball(Prime):
    """Растение: умеет пускать корни"""
    def root(self):
        print(self.name, " :пускаю корни")


class Computer(Reasonable):
    """Устройство, способное осуществялть логические операции"""


class Plane(Flying, Computer):
    """Летательный аппарат, на борту которого есть компьютер, способный выполнять какие-то логические операции"""


p = Human("Alex", '27')
p.addition(1003129, 99)
p.think()
p.take()
p.reproduction()
p.eat()
p.talk()

