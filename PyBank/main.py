# Importing modules 
import os
import csv

# Variables to calculate
total_months = 0
net_total = 0
changes_over_period = 0
greatest_increase = []
greatest_decrease = []


# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")

# Opening file
with open(csvpath) as csvfile:
    # Using CSV module to read file and save to new variable
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skipping the header before looping through data
    csvheader = next(csvfile)
    print(csvheader)

    # Loop through each row of data
    for row in csvreader:

        # Add 1 to keep count of each month (each row is a month)
        total_months += 1

        # Add/subtract the profit/loss column to value by converting string to float
        net_total += float(row[1])

        # Check if value is positive or negative, then append value to respective list
        if int(row[1]) > 0:
            greatest_increase.append(int(row[1]))
        else:
            greatest_decrease.append(int(row[1]))

print(f"Total months: {total_months}")
print(f"Net total: {net_total}")

print(max(greatest_increase))
print(min(greatest_decrease))