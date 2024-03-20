# Importing modules 
import os
import csv

# Variables to calculate
total_months = 0
net_total = 0
greatest_increase = 0
increase_month = ""
greatest_decrease = 0
decrease_month = ""
previous_value = 0
profit_loss_changes = []
current_change = 0


# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")

# Opening file
with open(csvpath) as csvfile:
    # Using CSV module to read file and save to new variable
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skipping the header before looping through data
    csvheader = next(csvfile)

    # Loop through each row of data
    for row in csvreader:

        # Add 1 to keep count of each month (each row is a month)
        total_months += 1

        # Add/subtract the profit/loss column to value by converting string to float
        net_total += int(row[1])

        # Calculate the change in profit/loss per month, add to list
        # 'if' function skips the calculations for the first row (where there are no changes)
        if previous_value != 0:
            current_change = int(row[1]) - previous_value
            profit_loss_changes.append(current_change)

        # Track the current greatest increases and decreases in changes and compare current change to them
            
        # Track for greatest increase change
        if current_change > 0:
            if greatest_increase != 0:
                if current_change > greatest_increase:
                    greatest_increase = current_change
                    increase_month = row[0]
            else:
                greatest_increase = current_change
                increase_month = row[0]
        
        # Track for greatest decrease change
        else:
            if greatest_decrease != 0:
                if current_change < greatest_decrease:
                    greatest_decrease = current_change
                    decrease_month = row[0]
            else:
                greatest_decrease = current_change
                decrease_month = row[0]

        # Change previous value before moving on to next row
        previous_value = int(row[1])

# Find the average of the profit/loss changes
average_changes = round((sum(profit_loss_changes)/len(profit_loss_changes)), 2)

# Print the calculations to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_changes}")
print(f"Greatest Increase in Profits: {increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})")


# Set path to text file
txtpath = os.path.join("analysis", "analysis.txt")

# Open text file to write to it
with open(txtpath, "w") as text_file:
    
    # Write to text file line by line
    text_file.write("Financial Analysis\n")
    text_file.write("----------------------------\n")
    text_file.write(f"Total Months: {total_months}\n")
    text_file.write(f"Total: ${net_total}\n")
    text_file.write(f"Average Change: ${average_changes}\n")
    text_file.write(f"Greatest Increase in Profits: {increase_month} (${greatest_increase})\n")
    text_file.write(f"Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})")