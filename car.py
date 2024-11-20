from vehicle import Vehicle

class Car(Vehicle):

    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)

        self.num_doors = num_doors

    #overriding the __str__ method
    def __str__(self):
        return f'{super().__str__()} Doors: {str(self.num_doors)}'