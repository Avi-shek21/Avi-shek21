import random
import emojis
print(emojis.encode("*Let's Play Stone:punch:, Paper:raised_hand: and Scissor:v:*\n"))
print(emojis.encode("Rules are Simple:exclamation:\n:one:Stone will win from Scissor but will loose from Paper.\n:two:Paper will win from Stone but will loose from Scissor.\n:three:Scissor will win from Paper but will loose from Stone."))

print("_______________________________________________________________________________")
computer = ["St","P","S"]

print(emojis.encode("Choose Any of Following:\nS for Scissor:v:\nP for Paper :raised_hand:\nSt for Stone:punch:\n"))
total_rounds = 6
user_win = 0
com_win = 0

for i in range(total_rounds):
	com = random.choice(computer)
	user = input(emojis.encode("Enter Your Choice from above:arrow_up:"))
	if user == "St":	
		if com == "S":
			user_win += 1
			print("Computer's recent Coice",com)
			continue
		elif com == "P":
			com_win +=1
			print("Computer's recent Coice",com)
			continue
		else:
			com_win +=0
			user_win +=0
			print("Computer's recent Coice",com)
			continue
	elif user == "P":
		if com == "S":
			com_win +=1
			print("Computer's recent Coice",com)
			continue
		elif com == "St":
			user_win += 1
			print("Computer's recent Coice",com)
			continue
		else:
			com_win +=0
			user_win +=0
			print("Computer's recent Coice",com)
			continue
	elif user == "S":
		if com == "P":
			user_win += 1
			print("Computer's recent Coice",com)
			continue
		elif com == "St":
			com_win += 1
			print("Computer's recent Coice",com)
			continue
		else:
			com_win += 0
			user_win += 0
			print("Computer's recent Coice",com)
			continue
	else:
		print("Invalid Input!")
		
		print("Based on upward result!\n")
		break
	i += 1

if user_win > com_win:
	print(emojis.encode("You won!:tada:\n"))
elif com_win==user_win:
	print(emojis.encode("It's a draw!:worried:\n"))
else:
	print(emojis.encode("You lose!:simple_smile:\n"))
c = input("Want More Details(Type Y or N)?")
if c == "Y":
	print("Numbers of rounds you won",user_win)
	print("Numbers of rounds computer won",com_win)
else:
	print(emojis.encode("Thanks for Using!:heart:"))
	
		