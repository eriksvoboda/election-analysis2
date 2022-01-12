# The data we need to retreive. 
#1. The total number of votes cast.
#2. A complete list of candidates who received votes.
#3. The percentage of votes each candidate won.
#4. The total number of votes each candidate won.
#5. The winner of the election based on popular vote.

#Add our dependencies
import csv
import os
#Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
#Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter
total_votes = 0

#declare a new list and print the candidate name from each row
candidate_options = []

#declare a new dictionary
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file
with open(file_to_load) as election_data:
    #read the file object with the reader function.
    file_reader = csv.reader(election_data)
#print each row in the csv file
    headers = next(file_reader)
#print each row in the CSV file
    for row in file_reader:
        #add the total vote count
        total_votes += 1

        #print the candidate name from each row
        candidate_name = row[2]

        #if the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            #Add it to the list of candidates
            candidate_options.append(candidate_name)

            #begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0

        #add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        #save the results to our text file
    with open(file_to_save, "w") as txt_file:
        #Print the final vote count to the terminal
        election_results = (
            f"\nElection Results\n"
            f"-----------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-----------------------\n")
        print(election_results, end="")
        # Save the final vote count to the text file
        txt_file.write(election_results)
    
        #determine the percentage of votes for each candidate by looping through the counts
        # 1. iterate through the candidate list
        for candidate_name in candidate_votes:
            #2. Retrieve vote count of a candidate
            votes = candidate_votes[candidate_name]
            #3. calculate the percentage of votes
            vote_percentage = float(votes) / float(total_votes) *100
            # To do: print out each candidate's name, vote count, and percentage of votes to the terminal
            candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            #print each candidate, their voter count, and percentage to the terminal
            print(candidate_results)
            # Save the candidate results to our text file
            txt_file.write(candidate_results)
            
            #Determine the winning ote count and candidate
            #1. determine if th evotes are greater than the winning count
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                #2. If true then set winning_count = votes and winning_percentage = vote_percentage
                winning_count = votes
                winning_percentage = vote_percentage
                #3. Set the winning_candidate equal to the candidate's name
                winning_candidate = candidate_name

        # To do: print out the winning candidate, vote count and percentage to terminal
        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")
        print(winning_candidate_summary)
        #Save the winning candidate's results to the text file
        txt_file.write(winning_candidate_summary)

