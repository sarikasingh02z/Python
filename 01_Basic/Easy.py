#EASY
# Python Program to Check Whether a Number is Positive or Negative
def check_numbers(n):
   if n>0:
      return "Positive" 
   else:
      return "Negative"

print(check_numbers(40))

#----------------------
#Write a Python function that accepts two integer numbers. If the product of the two numbers is less than or equal to 1000, return their product; otherwise, return their sum.
def sum_product(a,b):
   if a*b <=1000:
       return a*b
   else :
       return a+b

print(sum_product(50,5))

#-----------------------
#Iterate through the first 10 numbers. In each iteration, print the current number, the previous number, and their sum.
print("printing current and previous number sum in range (10)")
previous_num=0
for i in range(10):
      x_sum=previous_num+i
      print(f"current number {i} Previous number {previous_num} Sum:{x_sum}")
      previous_num=i

#------------------------
#Display only those characters which are present at an even index number in given string.
def even_index_chars(s):
    return s[0::2]

print(even_index_chars("pynative"))

#-----------------------------------------
    
# Write a function to remove characters from a string starting from index 0 up to n and return a new string.
def remove_chars(s,n):
    print("the original string is:", s)
    return s[n:]

print("removing character from a string")
print(remove_chars("pynative",3))

#-------------------------
#Write a program to swap the values of two variables, a and b, without using a third temporary variable.
def swap_var(a,b):
    print(f"the original a {a} and b {b}")
    a,b=b,a
    return a,b

print("the a and b after swap",swap_var(5,8))

#---------------------------
#Write a program that calculates the factorial of a given number (e.g., 5!) using a for loop.
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
    
print(factorial(5))

#----------------------------
#Given a list of integers, find and print both the largest and the smallest numbers.
print("find the largest and smallest number is a list")
num=[45,23,67,86,42]
largest=max(num)
smallest=min(num)

print("largest",largest)
print("smallest",smallest)