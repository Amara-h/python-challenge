# import os module to set a file path 
import os 
# import csv module to read csv files 
import csv
# set a path to budget_data.cvs
csv_path = os.path.join('..', 'PyRoll', 'election_data.csv')
#read csv file
with open(csv_path, 'r', newline='') as csv_reader:
     csv_reader = csv.reader(csv_path, delimiter=',')
#skip the header     
     next(csv_reader)











   





