class User:
    def __init__(self,city, pincode, state):
        
        self.city = city
        self.pincode = pincode
        self.state = state

    def address(self):
        return self.city, self.pincode, self.state

class Student(User):
    def __init__(self, name, gender, city, pincode, state):

        User.__init__(self, city, pincode, state)
        self.name = name
        self.gender = gender

    def Info(self):
        return self.name, self.gender

st1 = Student("Manas", "Male", "Mau", 275101, "UP")
print(st1.Info(), st1.address())
