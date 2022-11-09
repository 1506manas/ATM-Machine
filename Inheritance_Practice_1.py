class User:
    def Login(Self):
        print("Login")

    def Register(self):
        print("Register")

class Student(User):
    def Enroll(self):
        print("Enroll")

    def Review(self):
        print("Review")

st1 = Student()

st1.Enroll()
st1.Review()
st1.Register()
st1.Login()

