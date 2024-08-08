# Import libraries
import csv
import os

csvpath = os.path.join('.', 'Resources', 'election_data.csv')
# Read the CSV File
with open(csvpath, 'r') as file:
    reader = csv.DictReader(file)
    data = list(reader)

# Calculate the total number of votes cast
total_votes = len(data)
# Get a list of candidates who received votes
candidates = set([row['Candidate'] for row in data])
# Store candidate votes
candidate_votes = {candidate: 0 for candidate in candidates}
# Calculate the total number of votes each candidate won
for row in data:
    candidate_votes[row['Candidate']] += 1
# Calculate the percentage of votes each candidate won
candidate_percentages = {candidate: (votes / total_votes) * 100 for candidate,
                          votes in candidate_votes.items()}
# Find the winner of the election
winner = max(candidate_votes, key = candidate_votes.get)

# Print Analysis
print("Election Results")
print("----------------------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------------------")
for candidate in candidates:
    print(f"{candidate}: {candidate_percentages[candidate]:.3f}% ({candidate_votes[candidate]})")
print("----------------------------------------")
print(f"Winner: {winner}")
print("----------------------------------------")