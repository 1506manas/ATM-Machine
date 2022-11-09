#to solve quadratic equation "a(x^2)+bx+c=0"
import math
a=int(input("enter the coefficient of x^2:"))
b=int(input("enter the coefficient of x:"))
c=int(input("enter the constant value:"))
d=(b**2)-(4*a*c)
if(d>=0):
    d1=(-b- math.sqrt(d))/(2*a)
    d2=(-b+ math.sqrt(d))/(2*a)
    print("roots are:", d1,d2)
else:
    print("roots are  imaginary")
