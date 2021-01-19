import os
import csv

#Set path for CSV file
py_bank_path = os.path.join(".", "Resources", "budget_data.csv")

#Initialize date and profit/loss as list
date = []
profit_loss = []

#Initialize total amount of total profit and losses over the entire period
total_profitloss = 0

#Open CSV budget data file
with open(py_bank_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #separating header from list
    header = next(csvreader)

    #loop for rest of the rows
    for row in csvreader:    
        #creating list of dates and profits/losses
        date.append(row[0])
        profit_loss.append(row[1])
        #calculating total profit/losses
        total_profitloss+=int(row[1])

#calculating total number of months
total_months = len(date)

#Calculating the profit/loss change 
profit_loss_change_list = []
for i in range(1,len(profit_loss)):
    profit_loss_change = int(profit_loss[i]) - int(profit_loss[i-1])
    profit_loss_change_list.append(profit_loss_change)

#finding average change in profit/loss
average_change = sum(profit_loss_change_list)/len(profit_loss_change_list)

#excluding the first month in the date list to properly populate date with greatest increase/decrease
date.pop(0)

#finding the greatest and the least profit loss
greatest_increase = max(profit_loss_change_list)
greatest_decrease = min(profit_loss_change_list)

#finding the associated date with the greatest and the least profit loss
increasedate_index = profit_loss_change_list.index(greatest_increase)
decreasedate_index = profit_loss_change_list.index(greatest_decrease)

#print all analysis
print("Financial Analysis")
print("-"*20)
print(f"Total Months: {(total_months)}")
print(f"Total: ${(total_profitloss)}")
print(f"Average Change: ${round(average_change,2)}")
print (f"Greatest Increase in Profits: {date[increasedate_index]} (${greatest_increase})")
print (f"Greatest Decrease in Profits: {date[decreasedate_index]} (${greatest_decrease}")

#exporting final results to a txt file
output_path = os.path.join(".", "Analysis", "analysis_summary.txt")

with open(output_path, 'a') as file:
    file.write(f"Financial Analysis\n")
    file.write(f"--------------------\n")
    file.write(f"Total Months: {(total_months)}\n")
    file.write(f"Total: ${(total_profitloss)}\n")
    file.write(f"Average Change: ${round(average_change,2)}\n")
    file.write(f"Greatest Increase in Profits: {date[increasedate_index]} (${greatest_increase})\n")
    file.write(f"Greatest Decrease in Profits: {date[decreasedate_index]} (${greatest_decrease}\n")