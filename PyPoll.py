#1. The data we need to retrieve.

#Add dependencies
import csv
from functools import total_ordering
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Vote Counter
total_votes = 0

#Candidate Options and Votes
candidate_options = []

#Declare Dicitonary
candidate_votes={}

#Winning Candidate Vars
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

     # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        
        #2. Add to the total vote count.
        total_votes +=  1
        
        # Print the candidate name from each row
        candidate_name = row[2]

        if candidate_name not in candidate_options:

            #Add candidate name
            candidate_options.append(candidate_name)

            #Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        #Add votes
        candidate_votes[candidate_name]  +=1

#Calculate percentage of votes
for candidate_name in candidate_votes:
    
    #Retrieve cancdidate vote count
    votes = candidate_votes[candidate_name]

    #Calculate percentage
    vote_percentage = float(votes) / float(total_votes) * 100

    #Print name and vote percent
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    #Determine Winner
    if (votes > winning_count) and (vote_percentage > winning_percentage):

        winning_count = votes
        
        winning_percentage  = vote_percentage

        winning_candidate = candidate_name  

#Print Winner
winning_cadidate_summary = (
    f"--------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {round(winning_percentage, 1)}%\n"
    f"--------------------\n")

print(winning_cadidate_summary)