#input for starting year and how many years out

def int_input(prompt,error_message):
	#converts raw input from string into integer
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

Last_Year = Starting_Year + Years_from_Start

#measures of time

Time_Measure_Options = {"annual": 1, "semi-annual": 0.5, "quarter": .25}

Time_Measure = raw_input("How do you want to measure periods (quarter, semi-annual, annual?")

while (Time_Measure in Time_Measure_Options) == False:
	print "Please enter a valid period type"
	Time_Measure = raw_input("How do you want to measure periods (quarter, semi-annual, annual?")	 

years=[]

while Starting_Year < Last_Year:
	#function to add number of years to the list years
	years.append(Starting_Year)
	Starting_Year = Starting_Year + Time_Measure_Options[Time_Measure]

print years