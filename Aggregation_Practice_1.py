class Customer:
    def __init__(self, name, gender, address):
        self.name = name
        self.gender = gender
        self.address = address

class Address:
    def __init__(self, city, pincode, state):
        self.city = city
        self.pincode = pincode
        self.state = state

add = Address("Mau", 275101, "Uttarpradesh")
cust = Customer("Manas", "Male", add)


print(cust.address.city)
