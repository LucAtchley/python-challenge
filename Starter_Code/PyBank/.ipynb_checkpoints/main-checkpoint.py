import os
import csv

# Set the file path for the budget_data.csv file
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

# Initialize variables
total_months = 0
net_total = 0
changes = []
previous_profit_loss = 0

# Read the CSV file
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        # Calculate total months and net total profit/losses
        total_months += 1
        net_total += int(row[1])

        # Calculate changes in profit/losses
        current_profit_loss = int(row[1])
        if total_months > 1:
            change = current_profit_loss - previous_profit_loss
            changes.append(change)
        previous_profit_loss = current_profit_loss

# Calculate average change
average_change = sum(changes) / len(changes)

# Find greatest increase and decrease in profits
greatest_increase = max(changes)
greatest_decrease = min(changes)

# Find the corresponding dates for greatest increase and decrease
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        if int(row[1]) == greatest_increase:
            greatest_increase_date = row[0]
        if int(row[1]) == greatest_decrease:
            greatest_decrease_date = row[0]

# Print the Financial Analysis Report
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")