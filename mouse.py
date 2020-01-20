from animal import Animal

class Mouse(Animal):

    def __init__(self,name, age,height):

        super().__init__(name)
        self.age = age
        self.height = height

    def showInfo(self):
         super().showInfo()
         print("Age: "+ str(self.age))
         print("Height: "+ str(self.height))

    def move(self):
        print("Mouse moving...")
