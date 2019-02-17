import random
from time import sleep

# toppings
pepperoni = 0
mushrooms = 0
olives = 0
peppers = 0

# current toppings on pizza
pizza = [pepperoni, mushrooms, olives, peppers]


def new_game():
	# reset pizza toppings
	pepperoni = 0
	mushrooms = 0
	olives = 0
	peppers = 0

	
def topping_type():
	# for randomization:  pepperoni = 0, mushrooms = 1, olives = 2, peppers = 3
	return random.randint(0,3)


def topping_action():
	# if even toppings will be added, if odd toppings will be removed 
	action =  random.randint(0,10)

	if action%2 == 0:
		action = 1
	else:
		action = -1
	return action


def add_toppings(action, number, topping):
	pizza[topping] = pizza[topping] + (action * number)


def make_pizza():
	for turn in xrange(0, 19):
		
		# get all things needed during turn
		action = topping_action()    # add/remove
		number = random.randint(1,3) # number of that toppings added to pizza 
		topping = topping_type()     # type of topping added to pizza
		
		# get topping type as a string
		if topping == 0:
			topping_str = "PEPPERONI"
		elif topping == 1:
			topping_str = "MUSHROOMS"	
		elif topping == 2:
			topping_str = "OLIVES"
		elif topping == 3:
			topping_str = "PEPPERS"
		else:
			topping_str = "ERROR: Topping type."
		
		# if toppings are to be removed, check that there are enough toppings of that type on pizza
		if (action < 1) and (pizza[topping] < number):
			action = 1
			
		# each topping can have a max of 6 on pizza at a time, check to make sure adding the toppings will exceed max
		if pizza[topping] >= 6 or (pizza[topping]+number) >=6:
			action = -1

		add_toppings(action, number, topping)

		# print instructions
		if action > 0:
			print "Add", number, topping_str, "to your pizza."
			sleep(1.5)
		elif action < 0:
			print "Remove", number, topping_str, "from your pizza."
			sleep(1.5)
		else:
			print "ERROR: Action"
			return
	return

def playgame():
	print "Ready to make a pizza?"
	sleep(0.5)
	print "Here we go."
	sleep(1)
	
	make_pizza()
	
	print "Great job!"
	sleep(1)
	print "You should have", pizza[0], "pepperoni,", pizza[1], "mushrooms,", pizza[2], "olives and", pizza[3], "peppers."
	sleep(1)
	print "If you have those topping, CONGRATUALTIONS! You're a winner!"
	return

def main():
	playgame()
	sleep(0.5)
	
	while True:
		#print "Would you like to play again? (Y/N)"
		s = raw_input("Would you like to play again? (Y/N)").upper()
		if  s == "Y":
			playgame()
		else:
			break
	print "Thank you for playing."

if __name__== "__main__":
    main()
