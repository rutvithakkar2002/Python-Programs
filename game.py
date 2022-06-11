#Cows and Bulls is a pem and paper code breaking game usually playd between 2 players.
#In this, a player tries to guess a secret code number chosen by the second player.
#The ru;es are as follow:

#A player will create a secret code, usually 4 digit number..
#This number should have no repeated digits.

#Another player makes a guess(4 digit number) to creck the secret number. 
#upon making a guess, 2 hints will be provided ---->  cows & Bulls

#Bulls indicate the number of correct digits in the correct position.
#And cows indicate the number of correct digits in the wrong position.

# For example, if the secret code is 1234 and thr guessed number is 1246
# then we have 2 Bulls (for the exact matches of digits 1 and 2) and 1 cow( for the match of
# digit 4 in the wrong position)
# The player keeps on guessing untill the secret code is cracked.
# The player who guesses in the minimum of tries win.

import random
#returns list of digits of a number
def getDigits(num):
	return [int(i) for i in str(num)]

#Returns True if number has no duplicates digits otherwise false
def noDuplicates(num):
	num_li=getDigits(num)
	if len(num_li)==len(set(num_li)):
		return True
	else:
		return False
# Generates 4 digit number
#with no repeated digits
def generateNum():
	while True:
		num=random.randint(1000,9999)
		if noDuplicates(num):
			return num

# secret code
num=generateNum()
tries=int(input("Enter number of tries:" ))

#play game untill correct guess
# or till notries left
while tries>0:
	guess=int(input("Enter Your guess: "))
	if not noDuplicates(guess):
		print("Number should not have repeated digits. Try again")
		continue
	if(guess <1000 or guess>9999):
		print("Enter 4 digit number only. Try again")

	bull_cow=numOfBullsCows(num,guess)
	print(str(bull_cow[0])+"bulls "+str(bull_cow[1])+" cows")
