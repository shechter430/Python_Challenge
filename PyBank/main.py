import os
import csv

#Set path for CSV file
py_bank_path = os.path.join(".", "Resources", "budget_data.csv")

#Initialize date and profit/loss as list
date = []
profit_loss = []

#Initialize total amount of total profit/losses over the entire period
total_profitloss=0

#Open CSV budget data file
with open(py_bank_path, newline='') 
    csvreader = csv.reader(csvfile, delimiter=",")
    #separating header from list
    header = next(csvreader)

    #loop for rest of the rows
    for row in csvreader    
        #creating list of dates and profits/losses
        date.append(row[0])
        profit_loss.append (row[1])
        #calculating total profit/losses
        total_profitloss+int(row[1])


#total number of months
total_months = len(date)
print(total_months)
print(total)

#net total amount of


proft_loss_change_list = []
for i in range(1,len(profit_loss)):
    profit_loss_change = changes.append(int(profit_loss[i]) - (int(profit_loss[i-1]))
    profit_loss_change_list.append(profit_loss_change)
#print changes

average_change = sum(proft_loss_change_list)/len(proft_loss_change_list)
print(f"Average Change: $ {round(average_change,2)} ")

greatest_increase = max(profit_loss_change_list)
greatest_decrease = min(profit_loss_change_list)

print(greatest_increase)
print(greatest_decrease)


