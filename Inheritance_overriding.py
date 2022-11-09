class Phone:
    def __init__(self, price, brand, camera):
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a Phone")

class Smartphone(Phone):
    def buy(self):
        print("Buying a Smartphone")

s = Smartphone(10000, "Realme", 16)

s.buy()
