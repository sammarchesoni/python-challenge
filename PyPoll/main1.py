import os
import csv
pollpath = os.path.join('c:Homework 3_Instructions_PyPoll_Resources_election_data.csv')

total_votes = 0
candidates = []
poll = []
candidate_votes = []
candidate_percent = []
winner = ""

with open(pollpath, 'r') as csvfile:
   csvreader = csv.reader(csvfile, delimiter=',')
   header = next(csvreader)
   for row in csvreader:
       total_votes += 1
       candidates.append(row[2])

print("Election Results")
print("-------------------------")
print(f"Total Votes {total_votes}")
print("-------------------------")

# A complete list of candidates who received votes
candidates = sorted(candidates)

for i in range(total_votes):
    if candidates[i-1] != candidates[i]:
        poll.append(candidates[i])

# Calculate total number of votes each candidate won
for j in range(len(poll)):
    vote_count = candidates.count(poll[j])
    candidate_votes.append(vote_count)

# The percentage of votes each candidate won
for k in range(len(candidate_votes)):
    percent = (candidate_votes[k]/total_votes)*100
    candidate_percent.append(percent)

print(f"{poll.append(candidates)}: {candidate_percent.append(percent)}% ({candidate_votes.append(vote_count)})")


# The winner of the election based on popular vote.
popular_vote = candidate_votes.index(max(candidate_votes))
winner = poll[popular_vote]

print("-------------------------")    
print(f"Winner: {winner}") 
print("-------------------------")

output_file = os.path.join('c:Homework 3_Instructions_PyBank_Resources_analysis.text')
with open(output_file, 'w',) as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes {total_votes}\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Khan: {j}% {k}\n")
    txtfile.write(f"Correy: {j}% {k}\n")
    txtfile.write(f"Li: {j}% {k}\n")
    txtfile.write(f"O'Tooley: {j}% {k}\n")
    txtfile.write("-------------------------")
    txtfile.write(f"Winner: {winner}\n") 
    txtfile.write("-------------------------\n")