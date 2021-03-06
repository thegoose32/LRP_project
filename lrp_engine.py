from __future__ import print_function 
from decimal import Decimal


def decimal_input(prompt,error_message):
    #converts raw input from string into integer
    valid_input = False
    while valid_input == False:
        try:
            Raw_Input_String = raw_input(prompt)
            Raw_Input_Decimal = Decimal(Raw_Input_String)  #convert raw input (string) to integer
            valid_input = True
        except ValueError:
            print(error_message)
    return Raw_Input_Decimal



def percent_input(prompt,error_message):
    result = decimal_input(prompt,error_message)
    return result/Decimal('100.0')


def count_objects(prompt, error_message,name_objects,name_objects_list):
    #uses decimal_input to convert raw input to integer and then prompts user to name items in a list
    Count = decimal_input(prompt,error_message)
    input_count = 1
    while input_count < (Count+1):
        Program_Name = raw_input(name_objects+str(input_count)+"?")
        name_objects_list.append(Program_Name)
        input_count += 1

def yes_no_prompt(prompt):
    #function that requires a yes or no response
    yes_no = raw_input(prompt)
    while (yes_no == "Yes" or "No") == False:
        print("Please enter a Yes or No response")
        yes_no = raw_input(prompt)
    return yes_no

#input for starting year and how many years out

Starting_Year_Prompt = "What year do you want to start forecasting in?"
Starting_Year_Error = "Please enter a valid year"
Starting_Year = decimal_input(Starting_Year_Prompt,Starting_Year_Error)

Years_from_Start_Prompt = "How many years do you want to forecast?"
Years_from_Start_Error = "Please enter a valid range"
Years_from_Start = decimal_input(Years_from_Start_Prompt,Years_from_Start_Error)

Period_Error = "Please enter a valid period type"
Number_error = "Please enter a valid number"
Percent_error = "Please enter a valid percent"

Last_Year = Starting_Year + Years_from_Start

#measures of time

Time_Measure_Options = {
    "annual": Decimal('1.0'),
    "semi-annual": Decimal('0.5'),
    "quarter": Decimal('.25'),
}

Time_Measure = raw_input("How do you want to measure periods (quarter, semi-annual, annual?")

while (Time_Measure in Time_Measure_Options) == False:
    print(Period_Error)
    Time_Measure = raw_input("How do you want to measure periods (quarter, semi-annual, annual?")

years=[]

while Starting_Year < Last_Year:
    #function to add number of years to the list years
    years.append(Starting_Year)
    Starting_Year = Starting_Year + Time_Measure_Options[Time_Measure]

print(years)

number_of_periods = len(years)

def time_measure_convert(annual_cost):
    #converts annual costs to user-defined measurement
    return annual_cost * Time_Measure_Options[Time_Measure]

#Setting up Program Phases

program_phases = []
Program_Phases_Count_Prompt = "How many cost phases are in the lifecyle of your programs? (i.e. Discovery, GLP tox, Ph 1 study, etc."
Program_Phases_Prompt = "What label do you want for cost phase "

count_objects(Program_Phases_Count_Prompt,Number_error,Program_Phases_Prompt,program_phases)

print(program_phases)

program_phases_costs ={}

for program in program_phases:
    Program_Phases_Costs_Prompt = "For cost phase %(x)s, what is the cost per %(y)s period?" % {"x" : program, "y" : Time_Measure}
    Program_Phase_Cost = decimal_input(Program_Phases_Costs_Prompt,Number_error)
    program_phases_costs[program] = Program_Phase_Cost

print(program_phases_costs)

#Setting up Program Milestones
#(I think I can create a function to do this and program phases)

revenue_milestones = []
revenue_milestone_count_prompt = "How many revenue milestones do you want to track?"
revenue_milestone_label_prompt = "What label do you want for milestone "

count_objects(revenue_milestone_count_prompt,Number_error,revenue_milestone_label_prompt,revenue_milestones)

revenue_milestone_amounts ={}

for milestone in revenue_milestones:
    revenue_milestone_amount_prompt = "How much revenue is milestone %s worth?" % milestone
    revenue_milestone_amount = decimal_input(revenue_milestone_amount_prompt,Number_error)
    revenue_milestone_amounts[milestone] = revenue_milestone_amount

#Programs

Programs = []

Programs_Count_Prompt = "How many programs does the company have?"
Program_Name_Prompt = "What name do you want for program "

count_objects(Programs_Count_Prompt, Number_error,Program_Name_Prompt,Programs)

for program in Programs:
    program_name = program
    program = {}
    program_cost = program_name
    program_costs = {}
    program_milestone_revenue = {}
    for period in years:
        #User assigns what cost phase the program is in by period
        program_phase_by_period = raw_input("In %(x)s, what phase is program %(y)s in?" % {"x" : period, "y" : program_name})
        while (program_phase_by_period in program_phases_costs) == False:
            print("Please enter a valid program cost phase")
            program_phase_by_period = raw_input("In %(x)s, what phase is program %(y)s in?" % {"x" : period, "y" : program_name})
        program[period]= program_phase_by_period
        phase_cost = program_phases_costs[program_phase_by_period]
        program_costs[period] = phase_cost
    program_milestone_prompt = "Are there any milestones associated with this program?"
    program_milestones = yes_no_prompt(program_milestone_prompt)
    if program_milestones == "Yes":
        for milestone in revenue_milestones:
            program_milestone_achieved_prompt = "Is the %(x)s milestone achieved for program %(y)s?" % {"x" : milestone, "y" : program_name}
            program_milestone_achieved = yes_no_prompt(program_milestone_achieved_prompt)
            if program_milestone_achieved == "Yes":
                program_milestone_achieved_period_prompt = "In what period is the %(x)s milestone achieved for program %(y)s?" % {"x" : milestone, "y" : program_name}
                program_milestone_achieved_period = decimal_input(program_milestone_achieved_period_prompt,Period_Error)
                program_milestone_achieved_amount = revenue_milestone_amounts[milestone]
                program_milestone_revenue[program_milestone_achieved_period] = program_milestone_achieved_amount
            else:
                program_milestone_revenue[program_milestone_achieved_period]=0
    else:
        for period in years:
            program_milestone_revenue[period]=0
    print(program_milestone_revenue)

#FTEs

Starting_FTE_Prompt = "How many FTEs does the company start with?"
Starting_FTE_Error = "Please enter a valid FTE number"
Starting_FTEs = decimal_input(Starting_FTE_Prompt,Starting_FTE_Error)

FTE_growth_prompt = "What percent growth rate does the company grow?"
FTE_growth_rate = percent_input(FTE_growth_prompt,Percent_error)

FTE_cost_rate_prompt = "What is the annual cost of a FTE?"
FTE_cost_rate = time_measure_convert(decimal_input(FTE_cost_rate_prompt,Number_error))

FTE_cost_rate_growth_prompt = "What is the annual growth rate in FTE costs?"
FTE_cost_rate_growth = time_measure_convert(percent_input(FTE_cost_rate_growth_prompt,Percent_error))

FTEs = {}

def growth(base, growth_rate, results):
    base_period = Decimal('0.0')
    for period in years:
        results[period] = int(base*((Decimal('1') + growth_rate)**base_period))
        base_period = base_period + Time_Measure_Options[Time_Measure]
    return results

growth(Starting_FTEs,FTE_growth_rate,FTEs)

FTE_Cost = {}
growth(FTE_cost_rate,FTE_cost_rate_growth,FTE_Cost)

print(FTEs)
print(FTE_Cost)

#operating costs

Operating_costs_prompt = "What is the baseline operating cost per %s period?" % Time_Measure
Starting_operating_costs = decimal_input(Operating_costs_prompt,Number_error)

Operating_costs_rate_prompt = "What rate do baseline costs increase per %s period?" %Time_Measure
Operating_costs_growth_rate = percent_input(Operating_costs_rate_prompt,Percent_error)

Operating_costs ={}

growth(Starting_operating_costs,Operating_costs_growth_rate,Operating_costs)

print(Operating_costs)
#reporting

period_reported_prompt = "What period do you want financial results for?"
period_reported = decimal_input(period_reported_prompt,Period_Error)

while (period_reported in years) == False:
    print(Period_Error)
    period_reported = decimal_input(period_reported_prompt,Period_Error)

company_revenue = Decimal('0')
company_program_expense = Decimal('0')

print("Total Period Costs:")
for program in Programs:

    print("Program %(x)s revenue was %(y)s" % {"x" : program, "y" :program_milestone_revenue[period_reported]})
    print("Program %(x)s costs was %(y)s" % {"x": program, "y" : program_costs[period_reported]})
    company_revenue += program_milestone_revenue[period_reported]
    company_program_expense += program_costs[period_reported]

print("Total FTE costs were %s"  % FTE_Cost[period_reported])
print("Total operating costs were %s" %  Operating_costs[period_reported])

net_income = company_revenue - company_program_expense - FTE_Cost[period_reported]- Operating_costs[period_reported]
print("The Company's net income was %s" % net_income)
