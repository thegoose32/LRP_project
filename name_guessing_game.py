#guessing game!

A = raw_input("What word am I thinking of?")
B = "Jude"
C = 0

while A != B and C < 2:
	C += 1
	print "You have made %s guesses" %C
	print "Wrong guess! Try again."
	A = raw_input("What word am I thinking of?")

while A != B and C < 4:
	C += 1
	print "You only have %s guesses left" %(5-C)
	print "Here is a hint! The first letter is %s. Try again." % B[0]
	A = raw_input("What word am I thinking of?")

while A != B and C < 5:
	C += 1
	print "Last guess!"
	print "The first two letters are %s. Try again." % B[0:2]
	A = raw_input("What word am I thinking of?")


if A == B:
	print "You guessed correctly!"
else:
	print "Better luck next time!"