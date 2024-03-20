# Import modules
import os
import csv

# Define variables
total_votes = 0
candidates = {}

# Set path for file
csvpath = os.path.join("Resources", "election_data.csv")

# Opening file
with open(csvpath) as csvfile:

    # Use CSV module to read file
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skipping header
    csvheader = next(csvfile)

    # Loop through rows
    for row in csvreader:
        
        # Add 1 for each row to total_votes
        total_votes += 1

        # Create key for candidate if candidate is not in the dictionary
        if row[2] not in candidates.keys():
            candidates[row[2]] = 0

        # Add a vote for each candidate using their name as the key in 'candidates' dictionary
        candidates[row[2]] += 1

# Find the candidate with the most votes using max() on the "candidates" dictionary's values
election_winner = max(candidates.values())

# Print results to terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

# Iterate through dictionary to calculate the candidates' percentage of votes and print to terminal
for k, v in candidates.items():
    vote_percent = round(((v / total_votes) * 100), 3)
    print(f"{k}: {vote_percent}% ({v})")

    # Find the winning candidate by comparing the value to 'election_winner' and creating a variable with their name to print
    if v == election_winner:
        winner_name = k

# Print the winner using variable created
print("-------------------------")
print(f"Winner: {winner_name}")
print("-------------------------")