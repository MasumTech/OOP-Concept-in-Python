class Car():
    def __init__(self, name, manufacturer, color, year, cc):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color
        self.year = year
        self.cc = cc
        
    def start(self):
        print("Name: ",self.name)
        print("Manufacturer: ",self.manufacturer)
        print("Color: ",self.color)
        print("Year: ",self.year)
        print("CC: ",self.cc)
        print("Starting the engine...")
        print("----------------------")
         
    def brake(self):
        print("Name: ",self.name)
        print("Manufacturer: ",self.manufacturer)
        print("Color: ",self.color)
        print("Year: ",self.year)
        print("CC: ",self.cc)
        print("Braking the car...")
        print("----------------------")

    def drive(self):
        print("Name: ",self.name)
        print("Manufacturer: ",self.manufacturer)
        print("Color: ",self.color)
        print("Year: ",self.year)
        print("CC: ",self.cc)
        print("Deriving the car...")
        print("----------------------")

    def turn(self):
        print("Name: ",self.name)
        print("Manufacturer: ",self.manufacturer)
        print("Color: ",self.color)
        print("Year: ",self.year)
        print("CC: ",self.cc)
        print("Turning the car...")
        print("----------------------")

    def change_gear(self):
        print("Name: ",self.name)
        print("Manufacturer: ",self.manufacturer)
        print("Color: ",self.color)
        print("Year: ",self.year)
        print("CC: ",self.cc)
        print("Changing the gear...")
        print("----------------------")


my_car = Car("Corolla", "Toyota", "White", "2017", "1200")

print(my_car.start(), my_car.brake(), my_car.drive(), my_car.turn(), my_car.change_gear())



'''
---------------------------------------------------------------
class Car():
    def __init__(self, n, c):
        self.name = n
5        self.color = c

    def start(self):
        print("Name:", self.name)
        print("Color:", self.color)
        print("Starting the engine...")


car = Car("Colorra", "White")
car.year = 2017

print(car.name, car.color, car.year  )
 
--------------------------------------------------------------
class Car():
    def __init__(self, n, c):
        self.name = n
        self.color = c

    def start(self):
        print("Name:", self.name)
        print("Color:", self.color)
        print("Starting the engine...")


my_car1 = Car("Colorra", "White")
my_car1.start()
my_car2 = Car("Premio", "Black")
my_car2.start()
my_car3 = Car("Allion", "Blue")
my_car3.start()
--------------------------------------------------
class Car():
    def __init__(self, n, c):
        self.name = n
        self.color = c

    def start(self):
        print("Name:", self.name)
        print("Color:", self.color)
        print("Starting the engin...")


my_car = Car("Colorra", "White")
my_car.start()

-------------------------------------------------
class Car:

    def __init__(self, n, c):
        self.name = n
        self.color = c


    def start(self):
        print("Staring the engine")

my_car = Car("Corolla", "While")
print(my_car.name)
print(my_car.color)              
my_car.start()              
-----------------------------------


class Car:
    name = ""
    color = ""


    def __init__(self, name, color):
        self.name = name
        self.color = color

        
    def start(self):
        print("Starting the engine")

my_car = Car("Corolla", "White")
print(my_car.name)
print(my_car.color)
my_car.start()


class Car:
      name = ""
      color = ""

      def start(self):
          print("Starting the engine")


#creating a car object
my_car = Car()
my_car.name = "Allion"
print(my_car.name)
my_car.start()



class Car:
      name = ""
      color = ""

      def start():
          print("Starting the engine")




Car.name = "Axio"
Car.color = "Black"
print("Name of the car:", Car.name)
print("Color:", Car.color)
Car.start()

 --------------------------------
class Car:
    name = "Premio"
    color = "white"


    def start():
        print('Starting the engine')

print("Name of the car:", Car.name)
print("Color:", Car.color)
        
Car.start()
'''
