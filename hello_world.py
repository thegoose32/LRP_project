valid_input = False

while valid_input == False:
	try: 
		Input_Starting_Year = raw_input("What year do you want to start forecasting in?")
		Starting_Year = int(Input_Starting_Year)  #convert raw input (string) to integer
		valid_input = True
	except ValueError:	
		print "Please enter a valid year"

valid_input = False

while valid_input == False:
	try: 
		Input_Years_from_Start = raw_input("How many years do you want to forecast?")
		Years_from_Start = int(Input_Years_from_Start)
		valid_input = True
	except ValueError:
		print "Please enter a valid range"

Time_Measure = raw_input("How do you want to measure periods (quarter, semi-annual, annual?")

while Time_Measure != "quarter" and Time_Measure != "semi-annual" and Time_Measure != "annual":
	print "Please enter a valid period type"
	Time_Measure = raw_input("How do you want to measure periods (quarter, semi-annual, annual?")	 

Last_Year = Starting_Year + Years_from_Start

years=[]

if Time_Measure == "annual":
	time_increments = 1
elif Time_Measure == "semi-annual":
	time_increments = 0.5
else:
	time_increments = 0.25


while Starting_Year < Last_Year:
	#function to add number of years to the list years
	years.append(Starting_Year)
	Starting_Year = Starting_Year + time_increments

print years