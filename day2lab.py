# program to find the hypotenuse of a trianle given the A and B variable
#
import math
a = float(input("What is the value of A? "))
b = float(input("What is the value of B? "))
h = hypotenuse = math.sqrt(a**2+b**2)
area = (a*b)/2
perim = a + b + h 
print("Side A is " + str(a) + " inches")
print("Side B is " + str(b) + " inches")
print("The Hypotenuse is " + str(h) + " inches")
print("The Area is " + str(area) + " square inches")
print("The Perimeter is " + str(perim) + " inches")
