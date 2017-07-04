def int_input(prompt,error_message):
	valid_input = False
	while valid_input == False:
		try: 
			Raw_Input_String = raw_input(prompt)
			Raw_Input_Integer = int(Raw_Input_String)  #convert raw input (string) to integer
			valid_input = True
		except ValueError:	
			print error_message
	return Raw_Input_Integer

Starting_Year_Prompt = "What year do you want to start forecasting in?"
Starting_Year_Error = "Please enter a valid year"
Starting_Year = int_input(Starting_Year_Prompt,Starting_Year_Error)

Years_from_Start_Prompt = "How many years do you want to forecast?"
Years_from_Start_Error = "Please enter a valid range"
Years_from_Start = int_input(Years_from_Start_Prompt,Years_from_Start_Error)

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