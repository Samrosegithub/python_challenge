
# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv
csvpath = os.path.join('election_data.csv')
# /Users/home/Desktop/python_challenge/PyBank/Resources/election_data.csv
print("Test Demo: ", csvpath)
'PyBank/Resources/election_data.csv'
ballot_ID = []
total_country = []
candidate_options = []
total_candidate = []
list_1 = []
total_votes = 0
percent_votes = []
candidate_options = []
winner = []
candidate_votes = {}

# find out hwo to add items to dictionary add 1 + item to each to find # of items / total_votes

with open('election_data.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    # CSV Reader For Loop
for row in csvreader:
    total = + 1

    # TODO: All the logic happened here
    # (Profit loss - profit_losses -1)
    #ballot_ID += row[0]
    #country += row[1]
    #candidate += row[2]
    total_votes.append(row[0])
    total_candidate.append(row[2])
    if total_candidate in candidate_options:
        continue
    else:
        candidate_options.append(row[2])
        total = - 1
    for x in range(1, len(candidate_options)):
        count = 0
        for x in range(1, len(candidate_options)):
            if candidate_options[x] == total_candidate[x]:
                count += 1
        candidate_votes[candidate_options[x]] = count
    candidate_options.remove(candidate_options[0])
    percent_votes = candidate_options/total_votes
    print("Election Results")
    print(f'Total votes: [{percent_votes}')

for x in candidate_options:
print(percent_votes*100)
print(f'Winner: ',
candidate_options[percent_votes.index(max(percent_votes))])
total_votes = total_votes + 1
print(total_votes)