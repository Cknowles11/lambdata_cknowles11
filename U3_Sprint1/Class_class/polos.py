class Polo():

    # attribute
    # polo(color, size, brand)
    def __init__(self, color, size, brand):
        self.color = color
        self.size = size
        self.brand = brand

    # method
    def fold(self):
        print("Please fold the polo shirt")
    



if __name__=="__main__":
    polo1= Polo(color = "blue", size = "L", brand = "Ralph Lauren")
    polo1.fold()
    print(polo1.color)
    # pol1.sell()