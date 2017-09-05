simple_dataset ={
        'Start_Cash':  25000,
        'Collaborations': [
            {
                'Name': 'Collaboration 1',
                'ID': 'C001',
                'One_Time_Payments':[
                    {'Name': 'Upfront Payment', 'Amount': 50000, 'Period': 8}
                    ],
                'Ownership_Rights':[
                        {
                        'ID': 'CO001', 
                        'Name': 'US Rights', 
                        'Option_Payments':[
                            {'Name' : 'Option_Fee', 'Amount':  5000},
                            {'Name' : 'Option_Exercise', 'Amount':  10000},
                            ],
                        'Cost_Sharing':[
                            {'Phase_ID': 'Discovery', 'Cost_Share_Percent': 0},
                            {'Phase_ID': 'Preclincal', 'Cost_Share_Percent': 0},
                            {'Phase_ID': 'Phase_1', 'Cost_Share_Percent': 50},
                            {'Phase_ID': 'Phase_2', 'Cost_Share_Percent': 50},
                            {'Phase_ID': 'Phase_3', 'Cost_Share_Percent': 50}
                            ],
                        'Milestones': [
                            {'ID': 'M001', 'Name': 'GLP tox initiation', 'Amount': 5000, 'Link_to_Cost_Phase': 'Preclinical', 'Beg_or_End': 'Beg'},
                            {'ID': 'M002', 'Name': 'Phase 1 initiation', 'Amount': 10000, 'Link_to_Cost_Phase': 'Phase_1', 'Beg_or_End': 'Beg'},
                            {'ID': 'M003', 'Name': 'Phase 2 initiation', 'Amount': 20000, 'Link_to_Cost_Phase': 'Phase_2', 'Beg_or_End': 'Beg'},
                            ],
                    },
                        {
                        'ID': 'CO002', 
                        'Name': 'Worldwide Rights', 
                        'Option_Payments':[
                            {'Name' : 'Option_Fee', 'Amount':  5000},
                            {'Name' : 'Option_Exercise', 'Amount':  10000},
                            ],
                        'Cost_Sharing':[
                            {'Phase_ID': 'Discovery', 'Cost_Share_Percent': 0},
                            {'Phase_ID': 'Preclincal', 'Cost_Share_Percent': 0},
                            {'Phase_ID': 'Phase_1', 'Cost_Share_Percent': 100},
                            {'Phase_ID': 'Phase_2', 'Cost_Share_Percent': 100},
                            {'Phase_ID': 'Phase_3', 'Cost_Share_Percent': 100}
                            ],
                        'Milestones':[
                            {'ID': 'M001', 'Name': 'Phase 1 initiation', 'Amount': 5000, 'Link_to_Cost_Phase': 'Phase_1', 'Beg_or_End': 'Beg'},
                            {'ID': 'M002', 'Name': 'GLP tox initiation', 'Amount': 2500, 'Link_to_Cost_Phase': 'Preclinical', 'Beg_or_End': 'Beg'},
                            {'ID': 'M003', 'Name': 'Phase 2 initiation', 'Amount': 10000, 'Link_to_Cost_Phase': 'Phase_2', 'Beg_or_End': 'Beg'}
                            ],
                    }
                    ],
                'Collab_Programs':[
                        {
                            'ID': 'P001', 
                            'Ownership_Election': 'CO001', 
                            'Option_Payment_Timing': [
                                {'Name': 'Option_Fee', 'Period': 12},
                                {'Name': 'Option_Exercise', 'Period': 15}
                                ],
                            'Milestone_Timing': [
                                {'ID': 'M001', 'Period': 9 },
                                {'ID': 'M002', 'Period':15 },
                                {'ID': 'M003', 'Period':28 }
                                ],
                            },
                        {
                            'ID': 'P002', 
                            'Ownership_Election': 'CO002', 
                            'Option_Payment_Timing': [
                                {'Name': 'Option_Fee', 'Period': 18},
                                {'Name': 'Option_Exercise', 'Period': 21}
                                ],
                             'Milestone_Timing': [
                                {'ID': 'M001', 'Period':9 },
                                {'ID': 'M002', 'Period':15 },
                                {'ID': 'M003', 'Period':28 }
                                ]
                             }
                        ],
                },
            ],
        'Programs': [
            {
                'Name': 'Program 1',
                'ID': 'P001',
                'Phases': [
                    {'ID': 'Discovery', 'Start':1, 'End':8},
                    {'ID': 'Preclinical', 'Start': 9, 'End': 14},
                    {'ID': 'Phase_1', 'Start':15, 'End':27},
                    {'ID': 'Phase_2', 'Start':28, 'End':40},
                    {'ID': 'Phase_3', 'Start':41, 'End':53}
                ],
            },
            {
                'Name': 'Program 2',
                'ID': 'P002',
                'Phases': [
                    {'ID': 'Discovery', 'Start':1, 'End':8},
                    {'ID': 'Preclinical', 'Start': 9, 'End': 14},
                    {'ID': 'Phase_1', 'Start':15, 'End':27},
                    {'ID': 'Phase_2', 'Start':28, 'End':40},
                    {'ID': 'Phase_3', 'Start':41, 'End':53}
                ],
            },
            {
                'Name': 'Program 3',
                'ID': 'P003',
                'Phases': [
                    {'ID': 'Discovery', 'Start':1, 'End':8},
                    {'ID': 'Preclinical', 'Start': 9, 'End': 14},
                    {'ID': 'Phase_1', 'Start':15, 'End':27},
                    {'ID': 'Phase_2', 'Start':28, 'End':40},
                    {'ID': 'Phase_3', 'Start':41, 'End':53}
                ],
            },
        ],
        'Preclinical_Phases': [
            {
                'ID': 'Discovery',
                'Name': 'Discovery',
                'Spend': 80,
                'Periods': 6.0
            },
            {
                'ID': 'Preclinical',
                'Name': 'Preclinical',
                'Spend': 120,
                'Period': 6.0
            }
        ],
        'Clinical_Phases': [
            {
                'ID': 'Phase_1',
                'Name': 'Phase 1',
                'Patients': 180,
                'Patient_Cost': 2,
                'Periods': 12.0
            },
            {
                'ID': 'Phase_2',
                'Name': 'Phase 2',
                'Patients': 180,
                'Patient_Cost': 4,
                'Periods': 12.0
            },
            {
                'ID': 'Phase_3',
                'Name': 'Phase 3',
                'Patients': 180,
                'Patient_Cost': 6,
                'Periods': 12.0
            },
        ],
        'Incremental_Costs': [
                {'Name': 'Program 1 CMC overruns', 'Amount': 500, 'Program_ID': 'P001', 'Phase_ID': 'Preclinical'},
                {'Name': 'Biology complications', 'Amount': 200, 'Program_ID': 'P003', 'Phase_ID': 'Discovery'}
                ],
        'FTE': 4,
        'FTE_rate': 100,
        'FTE_increase_rate': 5.0,
        'FTE_rate_increase_rate': 5.0,
        'CapEx': 10,
        'CapEx_increase_rate': 2.0,
        'Operating_Expense': 10,
        'Operating_Expense_increase_rate': 5.0,
        'Financings': [
                {'Name': 'Series B', 'Period': 5, 'Amount': 50000},
                {'Name': 'Series C', 'Period': 12, 'Amount': 100000},
                {'Name': 'Series D', 'Period': 40, 'Amount': 100000},
                {'Name': 'IPO', 'Period': 52, 'Amount': 1000000}
        ]
    }



#number of periods is 15 years times 4 quarters/year = 60 quarters
periods = 60
period_list = []
x = 1

while x <= periods:
    period_list.append(x)
    x += 1

#Functions

def FTE_cost(FTE, FTE_rate):
    FTE_spend = FTE * FTE_rate
    return FTE_spend

def Trial_Costs(Patients,Patient_Cost):
    #calculate the trial costs
    Trial_Cost = (Patients * Patient_Cost)
    return Trial_Cost

def Period_Costs(Cost_Phase,Start,End,Program):
    #pulls the cost phase standard cost 
    Cost = 0
    if (Cost_Phase == 'Discovery') or (Cost_Phase == 'Preclinical'):
        for phase in simple_dataset['Preclinical_Phases']:
            if Cost_Phase == phase['ID']:
                Cost = phase['Spend']
    else:
        for trial in simple_dataset['Clinical_Phases']:
            if Cost_Phase == trial['ID']:
                Cost = (trial['Patients']*trial['Patient_Cost'])
    for program in simple_dataset['Incremental_Costs']:
        for phase in simple_dataset['Incremental_Costs']:
            if (Cost_Phase == phase['Phase_ID']) and (Program == program['Program_ID']):
                Cost += program['Amount']
    Period_Costs = Cost / (End - Start + 1)
    return Period_Costs

def cash(beg_cash,outflows,inflows):
    end_cash = beg_cash - outflows + inflows
    print (end_cash)

def annual_increases(database,base_amount,increase_amount):
    for period in period_list:
        #calculate FTE spend by period
        if period == 1:
            database[period] = base_amount
        elif ((period % 4.0) == 1) == True:
            database[period] = int((base_amount)*(increase_rate(increase_amount)**((period/4)-1)))
        else:
            database[period] = database[period-1]

def increase_rate(rate):
    increase_rate = (1.0+(rate/100.0))
    return increase_rate

def collab_payments(timing_dict, payment_dict):
    for collab_program in collaboration['Collab_Programs']:
        for payment in collab_program[timing_dict]:
            for ownership in collaboration['Ownership_Rights']:
                if (collab_program['Ownership_Election'] == ownership['ID']):
                    for item in ownership[payment_dict]:
                        if (payment['ID'] == item['ID']):
                            collab_inflows[payment['Period']] += item['Amount']


#collaboration inflows

collab_inflows = {}

for period in period_list:
    collab_inflows[period] = 0

for period in period_list:
    #add one time payments into collaboration inflows dictionary
    for collaboration in simple_dataset['Collaborations']:
        for one_time_payments in collaboration['One_Time_Payments']:
            if one_time_payments['Period'] == period:
                collab_inflows [period] = one_time_payments['Amount']

#collab_payments(simple_dataset['Collaborations'][0]['Option_Payment_Timing'],simple_dataset['Collaboration'][0]['Ownership_Rights'])
#how do I run a function that has lists and dictionaries?

for collab_program in collaboration['Collab_Programs']:
    #add option exercise and option fee payments into collaboration inflows dictionary
    for option_payment in collab_program['Option_Payment_Timing']:
        for ownership in collaboration['Ownership_Rights']:
            if (collab_program['Ownership_Election'] == ownership['ID']):
                for option_type in ownership['Option_Payments']:
                    if (option_payment['Name'] == option_type['Name']):
                        collab_inflows[option_payment['Period']] += option_type['Amount']

for collab_program in collaboration['Collab_Programs']:
    #add milestones earned into collaboration inflows dictionary
    for milestone_payment in collab_program['Milestone_Timing']:
        for ownership in collaboration['Ownership_Rights']:
            if (collab_program['Ownership_Election'] == ownership['ID']):
                for milestone in ownership['Milestones']:
                    if (milestone_payment['ID'] == milestone['ID']):
                        collab_inflows[milestone_payment['Period']] += milestone['Amount']
        
print (collab_inflows)

#program costs

program_cost = {}

for period in period_list:
    program_cost[period] = 0

for period in period_list:
    for program in simple_dataset['Programs']:
        for phase in program['Phases']:
            if (period >= phase['Start']) and (period <= phase['End']):
                program_cost[period] += (Period_Costs(phase['ID'],phase['Start'],phase['End'],program['ID']))

#FTE costs

FTE_spend = {}
FTE = {}
FTE_rate = {}

for period in period_list:
    #calculate the number of FTEs per period
    annual_increases(FTE,simple_dataset.get('FTE'),simple_dataset.get('FTE_increase_rate')) 
    #calculate the FTE rate for the period
    annual_increases(FTE_rate,simple_dataset.get('FTE_rate'),simple_dataset.get('FTE_rate_increase_rate'))
    #calculate total FTE spend for the period
    FTE_spend[period] = FTE[period]*FTE_rate[period]

#CapEx

CapEx_spend ={}

annual_increases(CapEx_spend,simple_dataset.get('CapEx'),simple_dataset.get('CapEx_increase_rate'))

#Operating Expenses

Operating_Exp_spend = {}

annual_increases(Operating_Exp_spend,simple_dataset.get('Operating_Expense'),simple_dataset.get('Operating_Expense_increase_rate'))

#Financings

Financings = {}

for event in simple_dataset['Financings']:
    Financings[event['Period']] = event['Amount']

#Cash balance

inflows ={}
outflows = {}
beg_cash = {}
end_cash ={}

for period in period_list:
    if period == 1:
        beg_cash[period] = simple_dataset.get('Start_Cash')
    else:
        beg_cash[period] = end_cash[period-1]
    try:
        inflows [period] = Financings[period]
    except KeyError:
        inflows [period] = 0
    outflows[period] = program_cost[period] + FTE_spend[period] + CapEx_spend[period] + Operating_Exp_spend[period]
    end_cash[period] = beg_cash[period] - outflows[period] + inflows[period]

print (end_cash)
