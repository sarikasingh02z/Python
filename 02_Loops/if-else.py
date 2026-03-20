#Print first 10 natural numbers using loop
def natural_numbers():
 for i in range (1,11):
    print(i)
natural_numbers()
 
#-----------------------------
#Write a Python code to print the following number pattern using a loop.
def number_pattern(n):
  for i in range(1, n+1):
    for j in range(1,i+1):
      print(j,end=" ")
    print()
number_pattern(5)   

#-------------------------------
#Calculate sum of all numbers from 1 to a given number
def add_nu (num):
  s=0
  for i in range(1,1+num):
    s+=i
  return s
add_nu(10)

#---------------------------------
#Print multiplication table of a given number
def multiplication(n):
  for i in range(1,11):
   print(f"{n} x {i} ={n*i}")
multiplication(2)

#-----------------------------------
#Display numbers from a list using a loop
numbers = [12, 75, 150, 180, 145, 525, 50]
for item in numbers:
    if item > 500:
        break
    elif item > 150:
        continue
    elif item % 5 == 0:
        print(item)

#----------------------------------
#Write a Python program to count the total number of digits in a number using a while loop.
num = 75869
count = 0
while num != 0:
    
    num = num // 10

    count = count + 1
print("Total digits are:", count)

#------------------------------------
#Write a Python program to print the reverse number pattern using a for loop.
n = 5
k = 5
for i in range(0,n+1):
    for j in range(k-i,0,-1):
        print(j,end=' ')
    print()

#----------------------------------
#Display a message “Done” after the successful execution of the for loop
for i in range(5):
    print(i)
else:
    print("Done!")