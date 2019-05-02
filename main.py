class Food(object):
    def __init__(self, name: str, food_type: str, heal: int):
        self.__name = name
        self.__food_type = food_type
        self.__heal = heal

    def get_name(self):
        return self.__name

    def get_food_type(self):
        return self.__food_type

    def get_heal_value(self):
        return self.__heal


# animal types = h - herbivorous, p - predator


class Animal(object):
    def __init__(self, name: str, what_eat: str, speed: int, health: int = 100):
        self.__name = name
        self.__what_eat = what_eat
        self.__speed = speed
        self.__health = health
        # Если травоядное, то животное съедобно
        if self.__what_eat.__eq__('h'):
            __eatable = True
        else:
            __eatable = False

    def get_name(self):
        return self.__name

    def isOvereating(self):
        if self.__health >= 100:
            return True
        else:
            return False

    def eat(self, food: Food):
        if self.__what_eat.__eq__(food.get_food_type()):
            self.__health += food.get_heal_value()
            if self.isOvereating():
                print(f'{self.get_name()} объелся!')
                self.__health = 100
        else:
            self.__health -= food.get_heal_value()


class Area(object):
    list_animals = []  # лист зверей
    list_foods = []  # лист еды

    def create_animal(self, name: str, what_eat: str, speed: int, heal: int = 100):
        animal = Animal(name, what_eat, speed)
        self.list_animals.append(animal)
    
    def delete_animal(self, animal:Animal):
        self.list_animals.pop(self.list_animals.index(animal))
        print(f'{animal.get_name()}, трагично погиб!')

    def create_food(self, name: str, food_type: str, heal: int):
        food = Food(name, food_type, heal)
        self.list_foods.append(food)

    def show_area(self):
        print('Здесь живут:')
        for animal in self.list_animals:
            print(animal.get_name())

area = Area()
area.create_animal('Медведь', 60, 'p')
area.show_area()

area.delete_animal(area.list_animals[0])
area.show_area()