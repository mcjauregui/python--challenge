#Import needed modules
import os
import csv
from collections import Counter
import sys

#Lists to store data
ballot_ids =[]
candidates = []

# Construct file path using os.path.join()
election_path = os.path.join("Resources","election_data.csv")

#Open CSV file and create lists out of needed data
with open(election_path, encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)  # Skip the header
    for row in csvreader:
        ballot_id = (row[0])
        candidate = (row[2])
        ballot_ids.append(row[0])
        candidates.append(row[2])

#Assign values to variables
total_votes = (len(set(ballot_ids)))
vote_recipients = set(candidates)
  
#print(total_votes)
#print(vote_recipients)

# Convert candidate set back to list
candidate_list = list(vote_recipients)

#Count occurrences of each value in candidates list by making a dictionary
#Assistance provided by https://bootcampspot.instructure.com/courses/4981/external_tools/313
#a. Initialize an empty dictionary candidate_counts to store counts of each candidate
candidate_counts_dict = {}
#b. Iterate over each candidate in candidates list
for candidate in candidates:
#c. For each candidate, check if value already exists in candidate_counts dictionary
# If does exist, increment count by 1 ; if it doesn't, add candidate to dictionary with count of 1
    if candidate in candidate_counts_dict:
        candidate_counts_dict[candidate] += 1
    else:
        candidate_counts_dict[candidate] = 1   
#print(candidate_counts_dict)

#Calculate each candidate's share of total votes
#a. Initialize new list to hold share_of_total calculation
share_of_total = []
# Iterate over both candidate (name) and candidate_count (votes per name) in dictionary 
for candidate, candidate_count in candidate_counts_dict.items():
# Each candidate has own cadidate_count; divide each candidate_count by total_votes 
    share = candidate_count / total_votes
# Form list out of the share values   
    share_of_total.append(share)
#print(share_of_total)

# Combine corresponding elements of candidate_counts dictionary and share_of_total list
# Assistance provided by https://bootcampspot.instructure.com/courses/4981/external_tools/313
# a. Extract keys and values from dictionary and zip them with list 
keys = candidate_counts_dict.keys()
values = candidate_counts_dict.values()
#  b. Zip keys and values with list
zipped_data = zip(keys, values, share_of_total)
# c. Convert zipped data to list for further processing
zipped_list = list(zipped_data)
#print(zipped_list)

#Isolate each row of zipped list
first_row = zipped_list[0]
second_row = zipped_list[1]
third_row = zipped_list[2]
#print(first_row)
#print(second_row)
#print(third_row)

# Identify which row contains greatest 'share_of_total' value in share_of_total list
# Assistance provided by https://bootcampspot.instructure.com/courses/4981/external_tools/313
max_share_of_total = 0
row_with_max_share = None
# Access 3rd element of tuple with 'row [2]' because that's where share_of_value is stored
for row in zipped_list:
    #Iterate through each row in zipped list and compare share_of_total value with current maximum value 
    #Update maximum value and store corresponding row each time new maximum is found
    if row[2] > max_share_of_total:
        max_share_of_total = row[2]
        row_with_max_share = row
#print(row_with_max_share)

#Isolate 'candidate' (name) from rest of row
candidate_with_max_share = row_with_max_share[0]

# Print analysis to look like results given
# Define election_analysis as string with formatting
# print the election_analysis to terminal and to txt output file
election_analysis = (
         f"\n\nElection Results\n"
         f"-------------------------\n"
         f"Total Votes: {total_votes}\n"
         f"--------------------------\n" 
         f"{first_row[0]}: {first_row[2]:.3%} ({first_row[1]})\n"
         f"{second_row[0]}: {second_row[2]:.3%} ({second_row[1]})\n"
         f"{third_row[0]}: {third_row[2]:.3%} ({third_row[1]})\n"
         f"--------------------------\n" 
         f"Winner: {candidate_with_max_share}\n"
         f"--------------------------\n" 
         ) 
print(election_analysis)
output_file_path = "Analysis/election_analysis.txt"
with open(output_file_path, 'w') as file:
     file.write(election_analysis)    