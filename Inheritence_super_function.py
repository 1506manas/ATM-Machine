class Grandfather:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        print(self.color)

class Father(Grandfather):
    def __init__(self, blood, color):
        super().__init__(color)
        self.blood = blood

    def get_blood(self):
        print(self.blood)
        
class Child(Father):
    def __init__(self, height, color, blood):
        super().__init__(blood, color)
        self.height = height

    def get_height(self):
        print(self.height)

st1 = Child(172, "fair", "O+")

st1.get_color()
st1.get_blood()
st1.get_height()
