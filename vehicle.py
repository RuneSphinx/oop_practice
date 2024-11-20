# Parent Class
class Vehicle:
    
    #class level attribute
    wheels = 4
    all_vehicles = []

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

        Vehicle.all_vehicles.append(self)

    #instance method that we can perform on the object
    def __str__(self):
        #return a string about the vehicle object
        return f'Vehicle Make:{self.make}, Model: {self.model}, Year: {self.year}'
    

    @classmethod
    def get_all_vehicles(cls):
        return cls.all_vehicles