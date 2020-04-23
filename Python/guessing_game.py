#Guessing game
import random
print('\t\t\tWelcome to the Guessing Game')
print('''There are 3 distinct level;
Easy
Medium
Hard.
			
You're to choose the level you want to play
			
''')
			
def level_easy():
	'''This is the easy level for the number guessing game'''
	number=random.randint(1,10)
	trial=0
	guesses=[]
	print('''In this level you're to guess a number between 1 and 10 and you have only 6 trial to get the correct number else you lost. ''')
	while True:
		guess=input(f'Make your guess,you have {str(6-len(guesses))} chance(s) to make the correct guess ')
		guesses.append(guess)
		trial+=1
		if guesses[-1] == str(number) and trial<=6:
			print('\nYou got it right.Congratulations!!!')
			break
		elif guesses[-1] != str(number) and trial<6:
			print('You got it wrong')
		else:
			print('Game over!!!')
			print(f'The correct number is {number}')
			break

def level_medium():
	'''This is the medium level for the number guessing game'''
	number=random.randint(1,20)
	trial=0
	guesses=[]
	print('''In this level you're to guess a number between 1 and 20 and you have only 4 trials to get the correct number else you lost. ''')
	while True:
		guess=input(f'\nMake your guess,you have {str(4-len(guesses))} chance(s) to make the correct guess ')
		guesses.append(guess)
		trial+=1
		if guesses[-1] != str(number) and trial<4:
			print('Your guess was wrong')
		elif guesses[-1] != str(number) and trial==4:
			print('Game over!!!')
			print(f'The correct number is {number}')
			break
		else:
			print('\nYou got it right.Congratulations!!!')
			break
			
def level_hard():
	'''This is the hard level for the number guessing game'''
	number=random.randint(1,50)
	trial=0
	guesses=[]
	print('''In this level you're to guess a number between 1 and 50 and you have only 3 trial to get the correct number else you lost. ''')
	while True:
		guess=input(f'\nMake your guess,you have {str(3-len(guesses))} chance(s) to make the correct guess ')
		guesses.append(guess)
		trial+=1
		if guesses[-1] != str(number) and trial<3:
			print('Your guess was wrong')
			if abs(int(guesses[-1])-number)>15:
				print('Cold guess!!!')
			elif abs(int(guesses[-1])-number)<5:
				print('Hot guess!!!')
			else:
					print('Warm guess!!!')
		elif guesses[-1] !=str(number) and trial==3:
			print('Game over!!!')
			print(f'The correct number is {number}')
			break
		else:
			print('\nYou got it right.Congratulations!!!')
			break	

def game():
	entry=input('\nEnter the level you want to play. e.g easy for easy level. ')
	if  entry[0].lower()=='e':
		level_easy()
	elif entry[0].lower()=='m':
		level_medium()
	else:
		level_hard()
#main
while True:
	game()
	entry=input('\nDo you wish to continue? Yes/No  ')
	if entry[0].lower()=='y':
		continue
	else:
		break
