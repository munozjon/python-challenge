# python-challenge

## Module 3 Challenge
For this assignment I analyzed data from 2 different CSV files using Python programming.

## PyBank
For this assignment, I analyzed a financial dataset in the form of a CSV file with two columns, "Date" and "Profit/Losses." I was instructed to find the total number of months included, the net total "profit/losses" across the entire period, the average changes in "profit/losses" month to month, the greatest increase in profits, and the greatest decrease in profits.

I begin by importing the modules I will need to set the path to the file and properly read the CSV file. Then, I set variables to count the months, the net total, values to find the current greatest increase and decrease in profits, as well as their respective months, the previous month, the current profit/lossses change, and a list to contain all the profit/loss changes. I then set the path to the file and open the file. After, I use the CSV module to read the file, and skip the header before looping through each row of data.

For each row in the loop, I add one to the total months counter and add the row's "profit/losses" value to the net total variable. I then calculate the change in profit/losses by subtracting the row's "profit/losses" value from the previous value (this part only runs if previous value contains a value to prevent it from running on the first row) and appending that value to the list of changes.

After, I check to see if the current change in profit is positive or negative. If it is positive, I check it against the variable for the current greatest increase in profits to see if it is greater. If so, I change the value for the current greatest increase to the current change. If it is negative, I instead check it against the current greatest decrease in profits to see if it is less than that, and change the variable to the current change if so. For both conditions, I also save the current row's "Month" value to use in the analysis. The conditions also account for if the variables for greatest increase and decrease are empty. After this, I set the current row's "profit/losses" value to the previous value variable and move on to the next row.

Once the code is finished looping through each row in the file, I exit the block of code reading the file and begin the analysis by calculating the average changes in profits and losses with the list of changes. I then print the findings to the terminal, including total months, net total, average changes, greatest increase in profits, and greatest decrease in profits (with both of their months). Finally, I set the path to the text file and open the file to write to it, where I write the same findings to the file as I printed to the terminal.

## PyPoll