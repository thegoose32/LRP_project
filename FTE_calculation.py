#FTE_calculation

GandA_FTEs = [2,2,5,7]
GandA_FTE_rate = 100000

FTE_Cost_Year = []

RandD_FTEs = [8,8,12,15]
RandD_FTE_rate = 120000

def total_FTE_cost(FTEs, FTE_rate):
	for FTE in FTEs:
		FTE_Cost_Year.append(FTE * FTE_rate)

total_FTE_cost(GandA_FTEs,GandA_FTE_rate)

print FTE_Cost_Year