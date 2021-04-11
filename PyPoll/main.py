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

     #set variable
     total_votes = 0
     current_candidate = ""
     condidate_votes = {}
     condidates = []

 # loop through the rows
for row in csv_reader:
     total_votes = total_votes + 1 
     current_candidate = row["candidate"]

     if current_candidate not in candidates:
          candidates.append(current_condidate)
          candidate_votes[current_condidate] = 1

     else:

            candidate_votes[current_candidate] = candidate_votes[current_candidate] + 1

# print the result 
print(f"Election results:")
print("-------------------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------------------")
for cv in candidate_votes:
    print(cv + ": " + str(round(((candidate_votes[cv]/total_votes)*100),3)) + "%" + " (" + str(candidate_votes[cv]) + ")") 
print("-------------------------------------")
 

#print the winner

list_votes = list(candidate_votes.value())

print("Winner is" + str(list(candidate_votes.keys())[list(candidate_votes.value()).index(max(list_votes))]))


# write the result in a text file
text_file = Path("python-challenge", "PyPoll", "Analysis", "Summary.txt")
with open(text_file, "w") as text_file:

    txt_file.write("Election results:")
  
    txt_file.write("-------------------------------------")
  
    txt_file.write("Total Votes: " + str(total_votes))
   
    
  
    for cv in candidate_votes:
        txt_file.write(cv + ": " + str(round(((candidate_votes[cv]/total_votes)*100),3)) + "%" + " (" + str(candidate_votes[cv]) + ")") 
           
    txt_file.write("Winner is " + str(list(candidate_votes.keys())[list(candidate_votes.values()).index(max(list_votes))]))
   





   





