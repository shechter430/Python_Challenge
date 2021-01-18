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

    #loop for rest of the rowsclear
    for row in csvreader:    
        #creating list of dates and profits/losses
        date.append(row[0])
        profit_loss.append(row[1])
        #calculating total profit/losses
        total_profitloss+=int(row[1])

#Print Statements
print("Financial Analysis")
print("-"*20)

#total number of months
total_months = len(date)
print(f"Total Months: {(total_months)}")
print(f"Total: ${(total_profitloss)}")

#Calculating the profit/loss change and finding average
profit_loss_change_list = []
for i in range(1,len(profit_loss)):
    profit_loss_change = int(profit_loss[i]) - int(profit_loss[i-1])
    profit_loss_change_list.append(profit_loss_change)

average_change = sum(profit_loss_change_list)/len(profit_loss_change_list)

    #Print average and greatest increase/decrease
print(f"Average Change: ${round(average_change,2)}")

date.pop(0)

greatest_increase = max(profit_loss_change_list)
greatest_decrease = min(profit_loss_change_list)

increasedate_index = profit_loss_change_list.index(greatest_increase)
decreasedate_index = profit_loss_change_list.index(greatest_decrease)

print (f"Greatest Increase in Profits: {date[increasedate_index]} (${greatest_increase})")
print (f"Greatest Decrease in Profits: {date[decreasedate_index]} (${greatest_decrease}")

