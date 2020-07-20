from random import randint
import sys


# Hey I am new to Github. 
# This is my first repo

text = input("Enter your name to say hello to ")
print(f"Hello {text}, how are you doing.")

while True:
	choice = input("Do you want to play the guessing game? y/n")
    if(choice == 'Y' or choice == 'y'):
		start = 1
		end = 10

		while True:
			try:
				guess_num = int(input(f"Enter a number between {start} and {end}. Lets see if we can match "))
			except ValueError:
				print("Enter a number please")
				continue
			guess_comp = randint(start,end)
			if guess_num == guess_comp:
				print("Its a match. Good game")
				break
			else:
				print(f"You guessed {guess_num}, I guessed {guess_comp}. Try Again.")
	elif(choice == 'N' or choice == 'n'):
		print("Bye")
		break
	else:
		print("Please enter in either Y or N")
		continue