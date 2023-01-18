
# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

#variables
months_total = 0
profit_Losses = 0
total_profits_sum = 0
difference = 0
difference_total = []
Change = []
greatest_increase = 0
greatest_decrease = 9999999999999999999

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    row_1 = next(csvreader)
    months_total += 1 
    
    for row in csvreader:
        index = 0
    profit_Losses += int(row_1[1])
    total_profits_sum = int(row[1])
    
    difference_total.append(row[0])
    
    difference = int(row[1]) - total_profits_sum
    change.append(difference)
    total_profits_sum = int(row[1]
    months_total += 1  
                            
    profit_Losses = profit_Losses + int(row[1])
    average = sum(Change)/len(Change)

total_profits_sum = sum(total_profits)

print(total_profits_sum)
greatest_decrease = min(difference_total)
greatest_increase = max(difference_total)
greatest_decrease = difference_total.index(greatest_decrease)
greatest_increase = difference_total.index(greatest_increase)

print("Financial Analysis")

print(f"Total Months: {months_total}\n")

print(f"Total Profit/Losess: ${profit_Losses}\n")

print(
    f"Average Change: ${round(sum(total_profits_sum)/len(total_profits_sum),2)}")

print(
    f"Greatest increase in Profits: {months_total[greatest_decrease]} (${(str(greatest_increase))})")

print(
    f"Greatest decrease in Profits: {months_total[greatest_decrease]} (${(str(greatest_decrease))})")
