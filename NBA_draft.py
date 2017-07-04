#NBA draft simulator

available_players = ["Lebron","Durant","Kawhai","Westbrook","Harden","George","Butler","Griffin","Paul","Curry"]
team_1 = []
team_2 = []

print "Welcome to the NBA draft"

selections = 0

while selections < 3:
	print "Available players:"
	print available_players
	print ""
	A = raw_input("Team 1 - which player do you select?")
	while (A in available_players) == False: #checks to ensure player selection is in list
		print "Please pick an available player"
		A = raw_input("Team 1 - which player do you select?")
	print "Team 1 selects %s" %A
	available_players.remove(A)
	team_1.append(A)
	print "Available players:"
	print available_players
	print ""
	B = raw_input("Team 2 - which player do you select?")
	while (B in available_players) == False: #checks to ensure player selection is in list
		print "Please pick an available player"
		B = raw_input("Team 2 - which player do you select?")
	print "Team 2 selects %s" %B
	available_players.remove(B)
	team_2.append(B)
	selections +=1

print "The NBA draft is complete"
print "Team 1:"
print team_1
print
print "Team 2:"
print team_2