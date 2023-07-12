# Polymorphism,inheritance and
import math
from abc import ABC, abstractmethod

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating...")


class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking...")


class Cat(Animal):
    def meow(self):
        print(f"{self.name} is meowing...")


# create animal objects
animal = Animal("animal")
dog = Dog("spot")
cat = Cat("kitty")

# Invoke call Eat Method
animal.eat()
dog.eat()
cat.eat()
cat.meow()
dog.bark()

# Example 2- car example


class Vehicle:
    def __init__(self, name):
        self.name = name

    def drive(self):
        print(f"{self.name} is driving...")


class Lorry(Vehicle):
    def start(self):
        print(f"{self.name} is starting...")

    def stop(self):
        print(f"{self.name} is stopping...")


class Car(Vehicle):
    def start(self):
        print(f"{self.name} is starting...")

    def accelerate(self):
        print(f"{self.name} is accelerating...")


vehicle = Vehicle("vehicle")
lorry = Lorry("Fusu")
car = Car("prado")

vehicle.drive()
lorry.drive()

# Example 3


"""class Vehicle:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def start(self):
        print(f"{self.brand} is starting...")

    def display_info(self):
        print("brand: {self.brand")
        print("color: {self.color}")

    def move(self):
        print("moving the vehicle")

    class Car(Vehicle):
        def __init__(self, brand, color, wheels):
            super().__init__(brand, color, wheels)
            self.wheels = wheels

        def display_info():
            super().display_info()
            print("wheels: {self.wheels}")

        def honk(self):
            print("Honking the horn")

    my_car = Car("Subaru", "blue", 4)

    # access and modify car attributes
    print(my_car.brand)
    print(my_car.color)"""

# Exercise
# Demonstrate using inheritance to calculate area and perimeter of circle and rectangle
# respectively(shape :circle)


class Shape:
    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_area(self):
        return self.width * self.length

    def calculate_perimeter(self):
        return 2 * (self.width + self.length)


# Example usage
circle = Circle(5)
print("Circle - Area:", circle.calculate_area())
print("Circle - Perimeter:", circle.calculate_perimeter())

rectangle = Rectangle(4, 6)
print("Rectangle - Area:", rectangle.calculate_area())
print("Rectangle - Perimeter:", rectangle.calculate_perimeter())


# multiple inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating...")


class Flyable:
    def fly(self):
        print(f"{self.name} is flying...")


class Bird(Animal, Flyable):
    def __init__(self, name, species):
        super().__init__(name)
        self.species = species

    def dispaly_info(self):
        super().disaly_info()
        print(f"species: {self.species}")
        print(f"name: {self.name}")

        # create the respective objects
        bird = Bird("dove", "bird")

        # invoke the bird method
        bird.eat()
        bird.fly()
        
#method overriding
class Animal:
    def make_sound(self):
        print("Animal is making a sound")

class Dog(Animal):
    def make_sound(self):
        print("Dog is barking")

class Cat(Animal):
    def make_sound(self):
        print("Cat is meowing")

def make_animal_sound(animal):
    animal.make_sound()

#create objects
animal = Animal()
dog = Dog()
cat = Cat()

#calling make_animal_sounf function
make_animal_sound(animal)
make_animal_sound(dog)
make_animal_sound(cat)

#Polymorphism - reusability,code that can work with different types of objects.
#Example on polymorphosm

#Method overriding - derived class provides its own implementation of a method that is already defined in its base class(super class)
#method overloading-multiple methods with same name but different parameters

#Example 
class Shape:
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_area(self):
        return self.width * self.length
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2
    
    def claculate_circumference(self):
        return 2 * math.pi * self.radius

    #create shape objects
    shape1 = Shape()
    shape2 = Rectangle(3,4)
    shape3 = Circle(5)

    #display area
    print("Area of rectangle:", shape2.calculate_area()) 
    print("Circle Area", shape3.calculate_area())       


#overloading functions
"""class Calculator:
    def add(self,x,y):
        return x + y

    def add(x,y,z):
        return x + y + z
    
#create object
calc = Calculator()

#display output
print(calc.add(1,2))
print(calc.add(1,2,3))"""

def add(x, y, z=None):
    if z is None:
        return x + y
    else:
        return x + y + z

# Example usage
print(add(1, 2))       # Two-operand addition
print(add(1, 2, 3))   

#Abstraction -allow you to focus on essential features and hide them from unecessary details
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Starting the car")
    
    def stop(self):
        print("Stopping the car")

class Truck(Vehicle):
    def start(self):
        print("Starting the truck")

    def stop(self):
        print("Stopping the truck")

#create the objects
car = Car()
truck = Truck()

#starting
car.start()
truck.start()

#stopping
truck.stop()
car.stop()

#Demonstrate abstraction using calculating area of a circle and recangles

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

circle = Circle(5)
print("Circle - Area:", circle.calculate_area())

rectangle = Rectangle(4, 6)
print("Rectangle - Area:", rectangle.calculate_area())

#create a recipt printing program with GUI interface

