class Suv():
    def __init__(self, make, model, year, color, num_wheels, num_seats):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.num_wheels = num_wheels
        self.num_seats = num_seats
    

    def drive(self):
        print("Turn on Suv")
        print("Shift into gear")
        print("Press gas pedal")


if __name__=="__main__":
    suv1= Suv(make = "Honda", model = "CRV", year = "2020", color = "Blue", num_wheels = "4", num_seats = "5 Seats")
    suv1.drive()
    print(suv1.make)
    print(suv1.model)
    print(suv1.num_seats)