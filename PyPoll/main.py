#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.

import os
import csv

#set path for CSV file
pypoll_path = os.path.join(".", "Resources", "election_data.csv")

#initialize lists
county = []
candidate_list = []
voter_id =[]

#open CSV election data file
with open(pypoll_path, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        #separating header 
        header = next(csvreader)

        #loop through rows to create lists
        for row in csvreader:
                voter_id.append(row[0])
                candidate_list.append(row[2])
                for x in csvreader:
                        if x not in candidate_list:
                                candidate_list.append(x)


print(candidate_list)                

#calculating total votes
total_votes = len(voter_id)






print(f"Total Votes: {total_votes}")








