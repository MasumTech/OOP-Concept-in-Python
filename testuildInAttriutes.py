class Customer:
    'This is Customer class'
    def __init__ (self,name,phone,address):
        self.name = name
        self.phone = phone
        self.address = address



john = Customer("Jhon", 1234567, "USA")


print("john.__dict__=", john.__dict__)

print("john.__doc__=", john.__doc__)

print("john.__class__", john.__class__)

print("john.__class__.__name__=", john.__class__.__name__)

print("john.__module__=", john.__module__)

    

    
