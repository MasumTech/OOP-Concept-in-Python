#An abstract class.

class AbstractDocument:
    def __init__(self,name):
        self.name = name


        #A method can not be used, because it always throws an error.
    def show(self):
        raise NotImplementedError("Subclass must implement abstract methid")



class PDF(AbstractDocument):

    #Override method of parent class

    def show(self):
        print("Show PDF document: ", self.name)


        

class Word(AbstractDocument):
    def show(self):
        print("Show Word document: ", self.name)


#---------------------------------------------------        
documents = [PDF("Python tutorial"), Word("Java IO Tutorial"),
             PDF("Python Date & Time Tutorial")]


for doc in documents:
    doc.show()
