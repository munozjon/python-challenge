"""
pseudo code

import modules

define variables:
total_votes = 0
candidates_dict = {}
candidate_1_votes = 0
candidate_2_votes = 0
candidate_3_votes = 0
candidate_votes_list = []

USE DICTIONARY: NAME BEING KEY AND VOTES BEING VALUE

set path to csv

open csv
    read csv
    skip csv header
    loop through csv rows
    total_votes += 1
    candidates_dict[row[2]] += 1

candidate_1_percentage = candidate 1 votes / total votes
candidate_votes_list.append (candidate 1 votes)

candidate_2_percentage = candidate 2 votes / total votes
candidate_votes_list.append (candidate 2 votes)

candidate_3_percentage = candidate 3 votes / total votes
candidate_votes_list.append (candidate 3 votes)

if max(candidate_votes_list) == candidate 1 votes:
    candidate 1 wins
elif max(candidate_votes_list) == candidate 2:
    candidate 2 wins
else:
    candidate 3 wins
"""

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
    print(csvheader)

    # Loop through rows
    for row in csvreader:
        
        # Add 1 for each row to total_votes
        total_votes += 1

        # Create key for candidate if candidate is not in the dictionary
        if row[2] not in candidates.keys():
            candidates[row[2]] = 0

        # Add a vote for each candidate using their name as the key in 'candidates' dictionary
        candidates[row[2]] += 1


election_winner = 0

# Print results to terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

# Iterate through dictionary to calculate the candidates' percentage of votes and print to terminal
for k, v in candidates.items():
    vote_percent = round(((v / total_votes) * 100), 3)
    print(f"{k}: {vote_percent}% (v)")
print("-------------------------")
print("")
print("-------------------------")