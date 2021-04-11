# import os module to set a file path 
import os 
# import csv module to read csv files 
import csv
# set a path to budget_data.cvs
budget_data = os.path.join('..', 'Pybank', 'budget_date.csv')
#read csv file
with open(budget_data, newline='') as csvreader:
     csvreader = csv.reader(budget_data, delimiter=',')
#skip the header     
     next(csvreader)

# creat lists to truck my variables 

total_months = []
total_profit = []
monthly_profit_change = []

# count total months and total profit 
for row in csv_reader:
     total_months.append(row[0])
     total_profit.append(int(row[1]))

# count total monthly profit change
for i in range(len(total_profit)-1):
     monthly_profit_change.append(total_profit[i+1]-total_profit[i])


#get the maximum amd the minimum monthly profit/loss change 

max_inc_value = max(monthly_profit_change)
min_dec_value = min(monthly_profit_change)

max_inc_month = monthly_profit_change.index(max(monthly_profit_change))+1
max_dec_month = monthly_profit_change.index(min(monthly_profit_change))+1


#print the result 

print("Financial Analysis")
print("------------------------------")
print(f"Total Months: {len(total_months)}")





















   





