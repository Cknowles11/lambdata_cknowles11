class Auto():

    def __init__(self, make, model, year, color, num_wheels):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.num_wheels = num_wheels
    

    def drive(self):
        print("Turn on %s" %self.make)
        print("Shift into gear")
        print("Press gas pedal")

class Truck(Auto):
    def __init__(self, make, model, year, color, num_wheels, bed_size):
        super().__init__(make, model, year, color, num_wheels)
        self.bed_size = bed_size

    #def drive(self):
        #print("Turn on Truck")
        #print("Shift into gear")
        #print("Press gas pedal")


class Suv(Auto):
    def __init__(self, make, model, year, color, num_wheels, num_seats):
        super().__init__(make, model, year, color, num_wheels)
        self.num_seats = num_seats
    

    #def drive(self):
        #print("Turn on %s" %self.make)
        #print("Shift into gear")
        #print("Press gas pedal")


if __name__=="__main__":
    suv= Suv("Honda", "CRV", 2020, "Blue", 4, num_seats = "5")
    suv.drive()
    print(suv.num_seats)
    #print(suv1.model)