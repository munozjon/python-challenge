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