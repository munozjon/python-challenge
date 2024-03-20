"""
pseudo code

import modules 'os' and 'csv'
declare variables for calculations

greatest_incr = 0
greatest_decr = 0
previous_value = 0

set path to the file

open csv file:
    use 'csv' module to make file readable, assigned to new variable
    skip header using 'next()'

    loop through each row in the file:
        
        add 1 to counter for total months

        add value in 'profit/loss' column to counter for net total with int()

       current_change = (this row's profit/loss value) - (previous_value)
        profit_loss_change.append(current_change)

        check if current_change is positive
            check if current_change > greatest_incr
                greatest_incr.append(row[0], current_change)

       else current change is negative
            check if current_change < greatest_decr
                greatest_decr.append(row[0], current_change)

        make current row's profit/loss value the 'previous_value' variable's value

        
output variables

"""

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


def financial_analysis():

    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${net_total}")
    print(f"Average Change: ${round((sum(profit_loss_changes)/len(profit_loss_changes)), 2)}")
    print(f"Greatest Increase in Profits: {increase_month} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})")

financial_analysis()

