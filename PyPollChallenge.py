# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter
total_votes = 0
# Create a list for Candidate and County
candidate_options = []
candidate_votes = {}
# Empty dictionaries for Candidate and County
county_options = []
county_votes = {}

# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Track the largest county and county voter turnout.
largest_county_turnout = ""
largest_county_vote = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    # Read the header row.
    header = next(reader)
    # Print each row in the CSV file
    for row in reader:
        # Add to the total vote count.
        total_votes = total_votes + 1
        # Get the candidate name from each row.
        candidate_name = row[2]
        county_name = row[1]

        # If the candidate does not match any existing candidate, add if statement
        # the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1  

        # if the candidate does not match any existing candidate, add if statement
        if county_name not in county_options:
            county_options.append(county_name)
            #Begin tracking each candidate's vote count.
            county_votes[county_name] = 0
        # Add a vote to that candidate's count 
        county_votes[county_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # After opening the file print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")

    print(election_results, end="")
    # After printing the final vote count to the terminal save the final vote count to the text file.
    txt_file.write(election_results)

    # Determine the percentage of votes per county.
    for county_name in county_votes:
        county_vote_count = county_votes[county_name]
        county_vote_percentage = float(county_vote_count)/float(total_votes)*100
        county_results=(
            f"{county_name}: {county_vote_percentage:.1f}% ({county_vote_count:,})\n")
        print(county_results)
        txt_file.write(county_results)

        if (county_vote_count > largest_county_vote):
            largest_county_vote = county_vote_count
            largest_county_tunout = county_name
        
    # Print the county with the largest turnout to the terminal.
    largest_county_tunout = (
        f"\n------------------------\n"
        f"Largest County Turnout: {largest_county_tunout}\n"
        f"------------------------\n")
    print(largest_county_tunout)
    
    txt_file.write(largest_county_tunout)
    
    #Iterate through candidate's list, determine the percentage of votes per candidate.
    for candidate_name in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        
        # Print out each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        # Save the candidate results tp our text file
        txt_file.write(candidate_results)
        # Determine winning vote count, winning percentage, and winning candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    # Print the winning candidate' results to the terminal 
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's result to txt file.
    txt_file.write(winning_candidate_summary)  
    