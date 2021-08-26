# Import modules
import os
import csv

# Define variables
total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

# Set path for file
csvpath = os.path.join('..', 'PyPoll', 'Resources', 'election_data.csv')

# Open the CSV
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row first
    csv_header = next(csvfile)

    # Read each row of data after the header
    for row in csvreader:
        
        # Calculate the total number of votes cast
        total_votes += 1
        
        # Calculate the total number of votes each candidate won
        if (row[2] == "Khan"):
            khan_votes += 1
        elif (row[2] == "Correy"):
            correy_votes += 1
        elif (row[2] == "Li"):
            li_votes += 1
        else:
            otooley_votes += 1
            
    # Calculate the percentage of votes each candidate won
    kahn_percent = khan_votes / total_votes
    correy_percent = correy_votes / total_votes
    li_percent = li_votes / total_votes
    otooley_percent = otooley_votes / total_votes
    
    # Calculate the winner of the election based on popular vote
    winner = max(khan_votes, correy_votes, li_votes, otooley_votes)

    if winner == khan_votes:
        winner_name = "Khan"
    elif winner == correy_votes:
        winner_name = "Correy"
    elif winner == li_votes:
        winner_name = "Li"
    else:
        winner_name = "O'Tooley" 

# Print Analysis
print(f"Election Results")
print(f"---------------------------")
print(f"Total Votes: {total_votes}")
print(f"---------------------------")
print(f"Kahn: {kahn_percent:.3%} ({khan_votes})")
print(f"Correy: {correy_percent:.3%} ({correy_votes})")
print(f"Li: {li_percent:.3%} ({li_votes})")
print(f"O'Tooley: {otooley_percent:.3%} ({otooley_votes})")
print(f"---------------------------")
print(f"Winner: {winner_name}")
print(f"---------------------------")

# Specify the file to write to
output_file = os.path.join('..', 'PyPoll', 'Analysis', 'results.txt')

# Open the file using "write" mode and specify the variable to hold the contents
with open(output_file, 'w',) as txtfile:

# Write output to txtfile
    txtfile.write(f"Election Results\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Kahn: {kahn_percent:.3%} ({khan_votes})\n")
    txtfile.write(f"Correy: {correy_percent:.3%} ({correy_votes})\n")
    txtfile.write(f"Li: {li_percent:.3%} ({li_votes})\n")
    txtfile.write(f"O'Tooley: {otooley_percent:.3%} ({otooley_votes})\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Winner: {winner_name}\n")
    txtfile.write(f"---------------------------\n")