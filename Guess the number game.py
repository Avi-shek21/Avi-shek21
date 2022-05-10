print("WELCOME TO GUESS THE NUMBER GAME")
guess = 1

while guess<=9:
	s = int(input("enter your number"))
	if s<12:
		print("you entered a small number plz increase it")
	elif s>12:
		print("you entered a greater number plz decrease it")
	elif s == 12:
		print("You rocked!")
	guess = guess + 1
if guess>9:
	print("Game over")