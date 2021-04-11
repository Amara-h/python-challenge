# import os module to set a file path 
import os 
# import csv module to read csv files 
import csv
# set a path to budget_data.cvs
csv_path = os.path.join('..', 'Pybank', 'budget_date.csv')
#read csv file
with open(csv_path, 'r', newline='') as csv_reader:
     csv_reader = csv.reader(csv_path, delimiter=',')
#skip the header     
     next(csv_reader)

# creat lists to truck my variables 

total_months = []
total_profit = []
monthly_profit_change = []


for row in csv_reader:
     total_months.append(row[0])
     total_profit.append(int(row[1]))


for i in range(len(total_profit)-1):
     monthly_profit_change.append(total_profit[i+1]-total_profit[i])
      















   





