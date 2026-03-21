#Print elements from a given list present at odd index positions
my_list= [10,20,30,40,50,60,70,80,90]
for i in my_list[1::2]:
   print(i)

#----------------------
#Calculate the cube of all numbers from 1 to a given number
n=6
for i in range(1,n+1):
   print(f"current numbers is {i} and the cube is{i**3}")

#----------------------
#Find the sum of a series of a number up to n terms
num=4
terms=5
s=0
for i in range(1,terms+1):
   print(num)
   s+=num
   num=num*10+4
print(f"sum of above series is{s}")

#---------------------------
#Write a program to print the following start pattern using the for loop
rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")

#-------------------
#Flatten a nested list using loops
def flatten_list(nested_list):
    
    flat_list = []  
    for element in nested_list:
        if isinstance(element, list): 
            for item in element:  
                flat_list.append(item)
        else:
            flat_list.append(element)  

    return flat_list

nested_list = [1, [2, 3], [4, 5, 6], 7, [8, 9]]
flattened = flatten_list(nested_list)
print("Flattened list:", flattened)

#Find largest and smallest digit in a number
def find_largest_smallest_digit(number):
 
  if number == 0:
    print("The number is zero. Largest and smallest digit is 0.")
    return 0, 0

  s_number = str(abs(number))  #
  largest_digit = int(s_number[0])
  smallest_digit = int(s_number[0])

  for digit in s_number[1:]:
    digit_int = int(digit)
    if digit_int > largest_digit:
      largest_digit = digit_int
    if digit_int < smallest_digit:
      smallest_digit = digit_int

  return largest_digit, smallest_digit

num1 = 9876543210
largest1, smallest1 = find_largest_smallest_digit(num1)
if largest1 is not None:
  print(f"Largest digit in {num1}: {largest1}")
  print(f"Smallest digit in {num1}: {smallest1}")
