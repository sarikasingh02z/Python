#medium
#Print Right Angled Triangle
def triangle(n):
    for i in range(1,n+1):
        print("*"*i)
triangle(6)

#------------------------
#Write a program to output the square of * (stars) of size 4 
def square(n):
    for i in range(n):
        print("*"*n)
square(4)

#------------------------
## Converting integer input into an float and vice versa
def conversion(a,b):
   a=float(a)
   b=int(b)
   print(f"int to float:{a}")
   print(f"float toint to :{b}")
conversion(5,8.9)

#--------------------------
#Given the radius of a circle and the area of a square, return True if the circumference of the circle is greater than the square's perimeter and False if the square's perimeter is greater than the circumference of the circle.
import math
def compare_shapes(radius,area):
    circumference=2 *math.pi *radius
    side=math.sqrt(area)
    perimeter=4*side
    return circumference>perimeter
print(compare_shapes(3,32))
print(compare_shapes(17,9))

#----------------------------
#Create a function that takes two arguments: the original price and the discount percentage as integers and returns the final price after the discount
def discounted_price(p,d):
    return p- (p*d/100)
print(discounted_price(1000, 10))  
print(discounted_price(500, 25))  


