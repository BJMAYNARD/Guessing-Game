#Basic Python Guessing Game

import random
import time

secret_number = random.randint (1, 50)
chances = 10

print ("Hello....welcome to the guessing game!")
time.sleep(2)
print ("I am thinking of a random number from 1 and 50.")
time.sleep(2)
print ("Do you think you can guess it?!")
time.sleep(2)
print ("Let's see....")
time.sleep(3)
game = True

while game is True:
	user_guess = int(input("What is your guess?"))
	if user_guess == secret_number:
		print("By golly --- you got it!")
		print("Would you like to play again?")
		answer = input ("yes or no? ")
		if answer == "yes":
			game = True
			chances = 10
		elif answer == "no":
			game = False
			(exit)
		
	elif user_guess > secret_number:
		print("Sorry but your guess is too high - try again")
		chances -= 1
		if chances > 0:
			print("Chances left: " + str(chances) + ".")
		else:
			print("Sorry - you didn't guess the secret number.")
			time.sleep(3)
			print("The secret number was " +str(secret_number) + ".")
			print("Would you like to play again?")
			answer = input ("yes or no? ")
			if answer == "yes":
				game = True
				chances = 10
			elif answer == "no":
				game = False
				(exit)
			
		
	elif user_guess < secret_number:
		print("Sorry but your guess is too low - try again")
		chances -= 1
		if chances > 0:
			print("Chances left: " + str(chances) + ".")
		else:
			print("Sorry - you didn't guess the secret number.")
			time.sleep(3)
			print("The secret number was " + str(secret_number) +  ".")
			print("Would you like to play again?")
			answer = input("yes or no? ")
			if answer == "yes":
				game = True
				chances = 10
			elif answer == "no":
				game = False
				(exit)
			
