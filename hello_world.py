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

Period_Error = "Please enter a valid period type"

Last_Year = Starting_Year + Years_from_Start

#measures of time

Time_Measure_Options = {"annual": 1, "semi-annual": 0.5, "quarter": .25}
Quarters = {.25: "Q2 ", .5: "Q3 ", .75: "Q4 ", 0.0: "Q1 "}
Halves = {.5: "H2 ", 0.0: "H1 "}

Time_Measure = raw_input("How do you want to measure periods (quarter, semi-annual, annual?")

while (Time_Measure in Time_Measure_Options) == False:
	print Period_Error
	Time_Measure = raw_input("How do you want to measure periods (quarter, semi-annual, annual?")	 

years=[]
periods = {}

while Starting_Year < Last_Year:
	#function to add number of years to the list years
	years.append(Starting_Year)
	Starting_Year = Starting_Year + Time_Measure_Options[Time_Measure]

for period in years:
	if Time_Measure == "quarter":
		periods[(str(Quarters[(period%1)]) + str(int(period-(period%1))))] = period
	elif Time_Measure == "semi-annual":
		periods[(str(Halves[(period%1)]) + str(int(period-(period%1))))] = period
	else:
		periods[("FY "+str(int(period)))] = period

print years #remove after test
print periods

number_of_periods = len(years)

def time_measure_convert(annual_cost):
	#converts annual costs to user-defined measurement
	return annual_cost * Time_Measure_Options[Time_Measure]

#FTEs

Starting_FTE_Prompt = "How many FTEs does the company start with?"
Starting_FTE_Error = "Please enter a valid FTE number"
Starting_FTEs = int_input(Starting_FTE_Prompt,Starting_FTE_Error)

FTE_growth_prompt = "What percent growth rate does the company grow?"
Percent_error = "Please enter a valid percent"
FTE_growth_rate = int_input(FTE_growth_prompt,Percent_error)

FTE_cost_rate_prompt = "What is the annual cost of a FTE?"
Number_error = "Please enter a valid number"
FTE_cost_rate = time_measure_convert(int_input(FTE_cost_rate_prompt,Number_error))

FTE_cost_rate_growth_prompt = "What is the annual growth rate in FTE costs?"
FTE_cost_rate_growth = time_measure_convert(int_input(FTE_cost_rate_growth_prompt,Percent_error))

FTEs = {}

def growth(base, growth_rate, results):
	base_period = 0.0
	for periods in years:
		results[periods] = int(base*((1+(float(growth_rate)/100))**base_period))
		base_period = base_period + Time_Measure_Options[Time_Measure]
	return results

growth(Starting_FTEs,FTE_growth_rate,FTEs)

FTE_Cost = {}
growth(FTE_cost_rate,FTE_cost_rate_growth,FTE_Cost)

print FTEs
print FTE_Cost

#operating costs

Operating_costs_prompt = "What is the baseline operating cost amount (annual)?"
Starting_operating_costs = int_input(Operating_costs_prompt,Number_error)

Operating_costs_rate_prompt = "What rate do basedline costs increase annually?"
Operating_costs_growth_rate = int_input(Operating_costs_rate_prompt,Percent_error)

Operating_costs ={}

growth(Starting_operating_costs,Operating_costs_growth_rate,Operating_costs)

print Operating_costs

#reporting

period_reported = raw_input("What period do you want financial results for?")

while (period_reported in periods) == False: #needs to be updated to periods; how do I link periods and years lists?
	print Period_Error
	period_reported = raw_input("What period do you want financial results for?")

def period_amount(period, numbers):
	period = periods[period]
	return numbers[period]

print period_amount(period_reported,FTE_Cost) + period_amount(period_reported,Operating_costs) #ask David - can I create a list with all cost types to make a function vs sum function?
