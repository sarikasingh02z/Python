#Write a program that searches for the first number greater than 100 in a list and stops the loop immediately when found. Print the number and its index.
numbers = [45, 67, 89, 123, 45, 200, 34]

for index, num in enumerate(numbers):
    if num > 100:
        print(f"First number > 100: {num} at index {index}")
        break

#write a program that prints all numbers from 1 to 20, but skips (continues) numbers that are multiples of 3.
for num in range(1, 21):
    if num % 3 == 0:
        continue
    print(num, end=" ")

# Write a program that checks if a number is prime using a for-else loop. If the number is prime, print "Prime found", otherwise print "Not prime". Use the else clause to execute when the loop completes without break.
num = 17

for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
        print(f"{num} is not prime")
        break
else:
    print(f"{num} is prime")

# Create a program that asks the user to guess a secret number (between 1-10). Give them 3 attempts. If they guess correctly, print "Correct!" and break. If they exhaust all attempts, print "Out of attempts!" using the else clause.
secret = 7
attempts = 3

while attempts > 0:
    guess = int(input("Guess the number (1-10): "))
    if guess == secret:
        print("Correct!")
        break
    attempts -= 1
    print(f"Wrong! {attempts} attempts left")
else:
    print("Out of attempts! The number was", secret)

#You have a 3x3 matrix. Write a program that searches for the number 5. Once found, break out of both loops and print "Found at (row, col)".
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

found = False
for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if matrix[row][col] == 5:
            print(f"Found at ({row}, {col})")
            found = True
            break
    if found:
        break

# Create a loop that prints numbers 1-10, but for multiples of 3, use pass as a placeholder. Then modify it to actually print something for multiples of 3.
# Modified version
for i in range(1, 11):
    if i % 3 == 0:
        print(f"{i} is multiple of 3")
    else:
        print(i)

# Write a program that continuously asks the user to enter names. Store them in a list. Stop when the user enters "quit". Use a flag variable to control the loop.
names = []
active = True

while active:
    name = input("Enter a name (or 'quit' to stop): ")
    if name.lower() == 'quit':
        active = False
    else:
        names.append(name)

print(f"Names collected: {names}")
