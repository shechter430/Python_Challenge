import os
import csv

#set path for CSV file
pypoll_path = os.path.join(".", "Resources", "election_data.csv")

#initialize lists
county = []
candidate = []


#open CSV election data file
with open(pypoll_path, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        #separating header 
        header = next(csvreader)


