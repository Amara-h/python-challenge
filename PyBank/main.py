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

# count months 
months = []
profit_loss = []
month = 0 
for row in csv_reader:
    months.append(row[0]) 
    profit_loss.append(row[1])
    month += 1









   





