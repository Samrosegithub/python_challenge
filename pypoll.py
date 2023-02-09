                            
#pypoll  
# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv           
csvpath = os.path.join('election_data.csv')
# /Users/home/Desktop/python_challenge/PyBank/Resources/election_data.csv
ballot_ID = []
votes = {}
total_votes = 0                            
candidate_options = 0
unique_candidate = 0
candidate = ""   
candidate_total = 0
greatest_votes = 0
                            
# find out hwo to add items to dictionary add 1 + item to each to find # of items / total_votes

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    row_1 = next(csvreader)    
    ballot_ID += (row_1[0])
    total_votes += 1
    # CSV Reader For Loop
    for row in csvreader:
        #ballot_ID += int(row_1[0])
        total_votes += 1  
        candidate = str(row[2])
        votes[candidate] = votes.get(candidate, 0) + 1
print(votes)
print(votes.keys())   

candidates = list(votes.keys())
can = candidates[0]
most = votes[can]
for x in candidates:
    if votes[x] > most:
        most = votes[x]
        can = x
print(can)
print(most)


winner = " "
total = 0
for k,v in votes.items():
    if v > total:
        total = v
        winner = k
print(winner)
print(total)

for k,v in votes.items():
    print("key=", k,"values=", v)
sum = 0
for k,v in votes.items():
    sum = sum + v
for can in candidates:
    print(votes[can]/sum*100)

can = candidates[0]

print(sum)

report = (
    f"{' Election Results ':^36}\n"
    f"{'--':-^36}\n"
    f"{'Total Votes:':12}{total:12,}{100:11,.2f}%\n"
    f"{'--':-^36}\n"
    f"{''.join(lines)}"
    f"{'--':-^36}\n"
    f"{'Winner:':12}{votes[winner]:12,}{winner:>12}\n"
    f"{'--':-^36}\n"
)


output = f""

Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
Charles Casper Stockham: 23.049% (85213)
Diana DeGette: 73.812% {total}
Raymon Anthony Doane: 3.139% (11606)
-------------------------
Winner: {winner}
""
print(output)

with open("Analysis/pypollanalysis.txt","w") as outputfile:
    outputfile.write(output)
