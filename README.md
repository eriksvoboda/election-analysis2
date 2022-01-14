# Election Analysis

## Project Overview
In addition to presenting the number of votes by candidate, the election commisson is interested in knowing the results by county. The purpose of this project is to provide the metrics, listed below, to the commission by using Python to extract the information from the CSV file and write it in a text file to present to the commission.

The Colorado Election commission has requested:
    - The voter turnout for each county
    - The percentage of votes from each county out of the total count
    - The county with the highest turnout

## Resources used in this project
- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code, 1.38.1

## Election Audt Results

Below are the results of the election audit; this includes the total votes, votes by candidate, votes by county, county with the largest turnout, and the election winner.

    - How many votes were cast in this congressional election?
        - 369,71 total votes
        
    - Breakdown of total votes and percent of votes by county
        - Jefferson: 10.5% (38,855)
        - Denver: 82.8% (306,055)
        - Arapahoe: 6.7% (24,801)
        
    - The county with the largest number of votes was:
        - Denver
        
    - Number of votes and percent of votes by candidate
        - Charles Casper Stockham: 23.0% (85,213)
        - Diana DeGette: 73.8% (272,892)
        - Raymon Anthony Doane: 3.1% (11,606)
        
    - The winning candidate, their vote count, and their percent of votes was:
        - Diana DeGette is the winner
        - Diana received 272,892 votes
        - Diana's percente of total votes is 73.8%
        
## Election-Audit Summary

In addition to examining county and candidate votes this script can be used to examine any election, given some modifications. This script could be utilized to examine voter turnout by age group and racial background. Additionally votes by registered voter party, city (which can be grouped into rural and urban areas), and voters' gender/sex can also be examined with this script provided some modifications.

Below is the a photo of the election results as saved in the text file as well as the full script itself. 

![](/Resources/election_analysis_output.png)

    # Add our dependencies.
import csv
import os

    # Add a variable to load a file from a path. And adding a variable to save the file to a path.
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")

    # Initialize a total vote counter.
total_votes = 0

    # Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

    # 1: Create a county list and county votes dictionary.
county_list = []
county_votes = {}

    # Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_county = 0
winning_percentage = 0
winning_county_percent = 0

    # 2: Track the largest county and county voter turnout.
largest_county_turnout = ""
county_voter_turnout = 0

    # Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_list:

            # 4b: Add the existing county to the list of counties.
            county_list.append(county_name)

            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0

        # 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1


    #Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

    # 6a: Write a for loop to get the county from the county dictionary.
    for county_name in county_votes:
            # 6b: Retrieve the county vote count.
            county = county_votes.get(county_name)
            # 6c: Calculate the percentage of votes for the county.
            county_percent = float(county) / float(total_votes) * 100
            county_results = (
                f"{county_name}: {county_percent:.1f}% ({county:,})\n")

            # 6d: Print the county results to the terminal.
            print(county_results, end="")
            # 6e: Save the county votes to a text file.
            txt_file.write(county_results)
            # 6f: Write an if statement to determine the winning county and get its vote count.
            #the error was that it wasn't indented enough, indentation matters
            if (county > winning_county) and (county_percent > winning_county_percent):
                winning_county = county
                winning_county_candidate = county_name
                winning_county_percent = county_percent

        # 7: Print the county with the largest turnout to the terminal.
    largest_county_turnout = (
        f"\n--------------------------\n"
        f"County with largest turnout: {winning_county_candidate}\n"
        f"----------------------------\n"
    )
    print(largest_county_turnout)
        # 8: Save the county with the largest turnout to a text file.
    txt_file.write(largest_county_turnout)

        # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

            # Retrieve vote count and percentage
            votes = candidate_votes.get(candidate_name)
            vote_percentage = float(votes) / float(total_votes) * 100
            candidate_results = (
                f"\n{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

            # Print each candidate's voter count and percentage to the
            # terminal.
            print(candidate_results)
            #  Save the candidate results to our text file.
            txt_file.write(candidate_results)

            # Determine winning vote count, winning percentage, and candidate.
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                winning_count = votes
                winning_candidate = candidate_name
                winning_percentage = vote_percentage

        # Print the winning candidate (to terminal)
    winning_candidate_summary = (
            f"\n-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")
    print(winning_candidate_summary)

        # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
