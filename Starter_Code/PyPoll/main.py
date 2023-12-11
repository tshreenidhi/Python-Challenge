# Import Libraries
import os
import csv

# Set File Path for Input and Output
csvpath = os.path.join("Resources" ,"election_data.csv")
output_file = "election_results.txt"

# Declaring the Variables and set their initial values
total_votes = 0
candidates = []
candidate_votes = {}
winner_count = 0
winner = ""




# Open the File
with open(csvpath) as csv_file:
    csv_reader = csv.DictReader(csv_file)
 
    #loop through to find the total votes
    for row in csv_reader:

        # Find the total vote count
        total_votes += 1

        candidate = row["Candidate"]
        # find and check on the first occurence of candidate name
        if candidate not in candidates:
            candidates.append(candidate)
            candidate_votes[candidate] = 1
        
        candidate_votes[candidate] = candidate_votes[candidate] + 1



#Create output file and also find the winning candidate
with open(output_file, 'w') as txt_file:
    #create header
    election_header = (
        f"Election Results\n"
        f"---------------\n")
    txt_file.write(election_header)
    #write the total number of votes
    txt_file.write("Total Votes : %d\n" % total_votes)   
    txt_file.write("\n---------------------\n")
    print(total_votes)
    
    #find the percentage of votes and make it 3 decimal points.
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        vote_percentage = float(votes)/float(total_votes)*100
        if (votes > winner_count):
            winner_count = votes
            winner = candidate
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output)
        txt_file.write(voter_output)
        
    winning_summary = (
        f"Winner: {winner}"
    )
    print(winning_summary)
    txt_file.write("---------------------\n")
    txt_file.write(winning_summary)
    txt_file.write("\n---------------------\n") 