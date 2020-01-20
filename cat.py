from animal import Animal

#Cat class extends from Animal.

class Cat(Animal):
      def __init__(self,name,age,height):
          
          #Call to constructor of parent class (Animal).
          #to assign value to attribute 'name' of parent class.

          super().__init__(name)
          self.age = age
          self.height = height


      #Override method.
      def showInfo(self):
          print("I'm " + self.name)
          print("Age: " + str(self.age))
          print("Height: "+ str(self.height))
          
