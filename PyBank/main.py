import os
import csv
bankpath = os.path.join('c:Homework 3_Instructions_PyBank_Resources_budget_data.csv')

months = []
pnl = []
total_change = []
avg_change = 0
profit = 0
loss = 0

# Method 2: Improved Reading using CSV module
with open(bankpath, newline= '') as csvfile:
   # CSV reader specifies delimiter and variable that holds contents
   csvreader = csv.reader(csvfile, delimiter=',')
   # Read The Header
   header = next(csvreader)
   # Go to the First Row
   row = next(csvreader)
   # Append to months and pnl 
   months.append(row[0])
   pnl.append(int(row[1]))
   # Set the rowas previous
   previous = int(row[1])
   # Iterate through every row
   for row in csvreader:
       # Append to months and pnl 
       months.append(row[0])
       pnl.append(int(row[1]))
       # Find the monthly change and append to total_change
       change = int(row[1])-previous
       total_change.append(int(change))
       # Set Current Row as previous
       previous = int(row[1])
# Calculate avg_change and format to two decimal points
avg_change = float("{0:.2f}".format(sum(total_change)/len(total_change)))
# Find the biggest increase and decrease
profit = max(pnl)
loss = min(pnl)
# Index the biggest increase and decrease
profit_month = pnl.index(max(pnl))+1
loss_month = pnl.index(min(pnl))+1
# Print the Analysis
print("Financial Analysis")
print("------------------------")
print(f"Total Months:{len(months)}")
print(f"Total: ${sum(pnl)}")
print(f"Average Change: {avg_change}")
print(f"Greatest Increase in Profits: {months[profit_month]} (${profit})")
print(f"Greatest Decrease in Profits: {months[loss_month]} (${loss})")
# Output file
output_file = os.path.join('c:Homework 3_Instructions_PyBank_Resources_analysis.text')
# Open output file to write to
with open(output_file, 'w',) as txtfile:
# Write New Data
   txtfile.write(f"Financial Analysis\n")
   txtfile.write(f"---------------------------\n")
   txtfile.write(f"Total Months:{len(months)}\n")
   txtfile.write(f"Total: ${sum(pnl)}\n")
   txtfile.write(f"Average Change: {avg_change}\n")
   txtfile.write(f"Greatest Increase in Profits: {months[profit_month]} (${profit})\n")
   txtfile.write(f"Greatest Decrease in Profits: {months[loss_month]} (${loss})\n")