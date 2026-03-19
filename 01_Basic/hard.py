#Check Palindrome string
def palindrom(word):
    reverse=word[::-1]
    return word==reverse

word=input("enter the word:")
print(palindrom(word))

#------------------------
#Write a function that takes a number and returns True if it's an Armstrong number.
def Armstrong_number(n):
    digits=str(n)
    power=len(digits)
    total=sum(int(d) **power for d in digits )
    return total==n
print(Armstrong_number(153))

#-------------------------
#Write a function that takes a number and returns True if it's a perfect number. A perfect number equals the sum of its divisors excluding itself.
def is_perfect(n):
    if n < 1: return False                      
    divisors = [i for i in range(1, n)          
                if n % i == 0]                 
    return sum(divisors) == n                   

print(is_perfect(6)) 

#--------------------------
#Write a function that takes a number and returns the next prime number after it.
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

def next_prime(n):
    num = n + 1
    while not is_prime(num):
        num += 1
    return num

print(next_prime(10))  

#---------------------------
#Write a function that takes two numbers and returns their GCD (Greatest Common Divisor) WITHOUT using any library.
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print(gcd(48, 18))