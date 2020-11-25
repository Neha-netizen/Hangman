import random
import time
def game(ran) :
	for i in ran:
		if i in 'AEIOU':
			print(i, end=' ')
		else:
			print('_', end=' ')
	trial = 8
	counter = 3
	counter2 = 3
	counter3 = 3
	alpha = ''
	result = 0
	print('')
	while trial>0:
		temp = 0
		count = -1
		if len(alpha)>0 :
			print("Your already entered letters are ",alpha)
		in1 = input("Your next guess is : ")
		in1 = in1.upper()
		if len(in1)>1 :
			temp=1
			print("Please enter a single letter")
		elif (in1.isalpha()) == False:
			temp = 1
			counter3 = counter3 - 1
			print('Not a letter and you have left ' + str(counter3) + ' chances to repeat a letter')
		elif in1 in alpha:
			temp = 1
			counter = counter - 1
			print('Repeated letter and you have left ' + str(counter) + ' chances to repeat a letter')
		elif in1 in 'AEIOU':
			temp = 1
			counter2 = counter2 - 1
			print('vowel and you have left ' + str(counter2) + ' chances to enter a vowel')
		else:
			alpha = alpha + in1
			count=0
			for i in ran:
				if i in alpha:
					print(i, end=' ')
				elif i in 'AEIOU':
					print(i, end=' ')
				else:
					count = count+1
					print('_', end=' ')
			print(' ')
		if in1 in ran:
			temp = temp+1
		if temp == 0:
			trial = trial - 1
			hangman(trial)
		if counter == 0:
			trial = 0
			print('lost')
		if counter2 == 0:
			trial = 0
			print('lost')
		if counter3 == 0:
			trial = 0
			print('lost')
		if trial == 0:
			print('Sorry you lost!')
		if trial>0 and count == 0:
			print('You won this round.')
			trial = 0
			result = 1
	return result

def hangman(photu):
	if (photu==7):
		print(' 0__|')
		print('    |')
		print('    |')
		print('    |')
		print('    |')
	elif(photu==6):
		print(' 0__|')
		print(' |  |')
		print('    |')
		print('    |')
		print('    |')
	elif (photu==5):
		print(' 0__|')
		print(' |  |')
		print(' |  |')
		print('    |')
		print('    |')
	elif (photu==4):    
		print(' 0__|')
		print(' |  |')
		print('/|  |')
		print('    |')
		print('    |')
	elif (photu==3):    
		print(' 0__|')
		print(' |  |')
		print('/|\ |')
		print('    |')
		print('    |')
	elif (photu==2):
		print(' 0__|')
		print(' |  |')
		print('/|\ |')
		print(' |  |')
		print('    |')
	elif (photu==1):
		print(' 0__|')
		print(' |  |')
		print('/|\ |')
		print('/|  |')
		print('    |')
	elif (photu==0):
		print(' 0__|')
		print(' |  |')
		print('/|\ |')
		print('/|\ |')
		print('    |')


print('Please enter your name')
name = input()
print('Welcome to the game of hangman ' + name)
time.sleep(2)
print('Do you think you are the best with words?')
time.sleep(2)
print('Try it yourself!')
time.sleep(2)



var = [['APPLE', 'MANGO', 'POMEGRANATE', 'STRAWBERRY', 'HONEYDEW'],
	['CRYPT', 'DWARVES', 'GYPSY', 'MEMENTO', 'PHLEGM'],
	['ZEALOUS', 'ZOMBIE', 'JINX', 'AWKWARD', 'HYPHEN']]

for level in range(3) :
	ran = random.choice(var[level])
	print('You are in level ',str(level+1),' and your word is:')
	time.sleep(1)

	result = game(ran)
	if result == 0 :
		print("Loser!!")
		break

if result == 1 :
	print("Yipee! You won this game.")
           
            
      
    

        
      
    
