# Parent Class
class Vehicle:
    
    #class level attribute
    wheels = 4

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    #instance method that we can perform on the object
    def __str__(self):
        #return a string about the vehicle object
        return f'Vehicle Make:{self.make}, Model: {self.model}, Year: {self.year}'
    


