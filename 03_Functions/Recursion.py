#Write a recursive function factorial(n) that returns n! (n × (n-1) × ... × 1).

def factorial(n):
    
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  
print(factorial(3)) 

#Write a recursive function sum_to_n(n) that returns the sum of all numbers from 1 to n.

def sum_to_n(n):
    if n <= 0:
        return 0
    return n + sum_to_n(n - 1)

print(sum_to_n(5))   
print(sum_to_n(10))

#Write a recursive function fibonacci(n) that returns the nth Fibonacci number. (Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21...)

def fibonacci(n):
   
    if n == 0:
        return 0
    if n == 1:
        return 1
    # Recursive case
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(0))  
print(fibonacci(1))  
print(fibonacci(6))  

#Write a recursive function power(base, exp) that returns base raised to the power exp. (Don't use the ** operator)
def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

print(power(2, 3))   
print(power(5, 0))   
print(power(3, 4))   

#Write a recursive function sum_of_digits(n) that returns the sum of all digits in a number.

def sum_of_digits(n):
    if n < 10:
        return n
    return n % 10 + sum_of_digits(n // 10)

print(sum_of_digits(123))   
print(sum_of_digits(4567)) 
print(sum_of_digits(9))     

#Write a recursive function is_palindrome(s) that returns True if the string is a palindrome , False otherwise

def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

print(is_palindrome("racecar"))   
print(is_palindrome("hello"))     
print(is_palindrome("a"))         
print(is_palindrome(""))          