import os
import csv

#set path for CSV file
pypoll_path = os.path.join(".", "Resources", "election_data.csv")

#initialize lists
voter_id = []
candidates = []
candidate_list = {}

#open CSV election data file
with open(pypoll_path, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        #separating header 
        header = next(csvreader)

        #loop through rows to create lists
        for row in csvreader:
                voter_id.append(row[0])
                candidates.append(row[2])

        print("Election Results")
        print("-"*20)

        #calculating total votes and printing
        total_votes = len(voter_id)
        print(f"Total Votes: {total_votes}")
        print("-"*20)

        #getting each candidate name
        candidate_unique = set(candidates)
        
        #looping through dictionary to determine each candidates vote count, percentage and printing totals
        for vote in candidate_unique:
                candidate_list[vote] = candidates.count(vote)
        for key, value in candidate_list.items():
                print(f'{key}: {"{:.3f}".format(float(value/total_votes)*100)}% {value}')
        
        #determining winner and printing result
        winner = max(candidate_list, key=candidate_list.get)              
        print("-"*20)
        print(f"Winner: {winner}")

#exporting to txt file
output_path = os.path.join(".", "Analysis", "analysis_summary.txt")
with open(output_path, 'a') as file:
        file.write(f"Election Results\n")
        file.write(f"--------------------\n")
        file.write(f"Total Votes: {total_votes}\n")
        file.write(f"--------------------\n")
        file.write(f'{key}: {"{:.3f}".format(float(value/total_votes)*100)}% {value}\n')
        file.write(f"--------------------\n")
        file.write(f"Winner: {winner}\n")
