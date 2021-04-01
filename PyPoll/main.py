# Import dependencies
import os, csv
from pathlib import Path 

# Assign file location with the pathlib library
csv_file_path = Path("python-challenge", "PyPoll", "election_data.csv")

# Declare Variables 
total_votes = 0 
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

# Open csv in default read mode with context manager
with open(csv_file_path,newline="", encoding="utf-8") as election_data:

    # Store data under the csvreader variable
    csvreader = csv.reader(election_data,delimiter=",") 

    # Skip the header so we iterate through the actual values
    header = next(csvreader)     

    # Iterate through each row in the csv
    for row in csvreader: 

        # Count the unique Voter ID's and store in variable  called total_votes
        total_votes +=1

        # We have four candidates if the name is found, count the times it appears and store in a list
        # We can use this values in our percent vote calculation in the print statements
        if row[2] == "Khan": 
            khan_votes +=1
        elif row[2] == "Correy":
            correy_votes +=1
        elif row[2] == "Li": 
            li_votes +=1
        elif row[2] == "O'Tooley":
            otooley_votes +=1

 # To find the winner we want to make a dictionary out of the two lists we previously created 
candidates = ["Khan", "Correy", "Li","O'Tooley"]
votes = [khan_votes, correy_votes,li_votes,otooley_votes]

