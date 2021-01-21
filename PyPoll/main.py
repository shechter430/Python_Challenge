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
candidate = []
total_votes = 0

#open CSV election data file
with open(pypoll_path, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        #separating header 
        header = next(csvreader)

        for row in csvreader:
                total_votes += 1


print(f"Total Votes: {total_votes}")








