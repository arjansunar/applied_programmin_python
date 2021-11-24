print("_________________Developed by Arjan Gahatraj_______________")
# 1. Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they 
# will turn 100 years old.
print("Enter your name and age:")
name = input("Name: ")
age  = int(input("Age: "))

current_year= 2021
if (age <100):
    print(f'{name} will turn 100 in year {100 - age + current_year}')
else: 
    print(f'You are already over 100 years')

# 2. Write a Python program to print the following string in a specific format
 
print(
'''
    Twinkle, twinkle, little star,
      How I wonder what you are!
             Up above the world so high,
             Like a diamond in the sky.
    Twinkle, twinkle, little star,
      How I wonder what you are
'''
)

# 3. Write a Python program to guess a number between 1 to 9.

import random


target = random.randint(1,9)

# game loop
while True:
	usr_guess = int(input("Enter a guess: "))
	if (usr_guess > target):
    	 print("Too high") 
	elif (usr_guess < target):
    	 print("Too low") 
	else:
		print("well guessed!")
		break
		 
# 4. Python Program to Convert Decimal to Binary, Octal and Hexadecimal

val= int(input("Enter a value: "))

print(f'{val} in binary is: {bin(val)}')
print(f'{val} in octal is: {oct(val)}')
print(f'{val} in hexadecimal is: {hex(val)}')
