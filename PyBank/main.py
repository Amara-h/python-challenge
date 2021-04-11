# import os module to set a file path 
import os 
# import csv module to read csv files 
import csv
# set a path to budget_data.cvs
budget_data = os.path.join('..', 'PyBank', 'budget_date.csv')
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


#print the results 

print("Financial Analysis")
print("------------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change)),2}")
print(f"Greatest Increase in Profit: {total_months[max_inc_month]} (${(str(max_inc_value))})")
print(f"Greatest Decrease in Profit: {total_months[max_dec_month]} (${(str(max_dec_value))})")


# create text file

text_file = Path("python-challenge", "Pybank", "analysis", "Summary.txt")

with open(text_file, "w") as file:
     file.write("Financial Analysis")
     file.write("----------------------------")
     file.write(f"Total Months: {len(total_months)}")
     file.write(f"Total: ${sum(total_profit)}")
     file.write(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change)),2}")
     file.write(f"Greatest Increase in Profit: {total_months[max_inc_month]} (${(str(max_inc_value))})")
     file.write(f"Greatest Decrease in Profit: {total_months[max_dec_month]} (${(str(max_dec_value))})")


















   





