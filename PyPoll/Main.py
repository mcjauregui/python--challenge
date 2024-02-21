#PyPoll Challenge
#Import needed modules
import os
import csv
from collections import Counter
import sys

#Instructions for reading CSV module
election_csv = os.path.join("Resources","election_data.csv")

#Lists to store data
ballotID = {}
candidate = {}

#Open the csv filename 'election_csv' and load into file object 'csvfile'
with open(election_csv) as csvfile:
#Create reader object 'csvreader' by passing file object to the reader function    
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)  #Skip the header
#Use for loop on reader object 'csvreader' to get each row 
#Does this create the dictionary or just two lists??? To what are we appending rows?  
    for row in csvreader:
        ballotID.append(row[0]) #ballotID from first row (row zero)
        #candidate_Name = (row[2]) 
        candidate.append(row[2]) #candidate_Name is the third row (row two)

from collections import Counter
z = {candidate}
Counter(z)
print(Counter(z))

unique_candidate = 0
votes_per_candidate = 0
all_ballots_cast = 0
cand_percentage = 0

for x in set({candidate}):
    unique_candidate.append(x)
    #Count votes per unique candidate
    candidate_votes = candidate.count(x)
    votes_per_candidate.append(y)
    #Count all ballots cast in election
    all_ballots_cast = Counter(z)
    #Get % of total ballots cast per candidate
    candidate_percentage = (candidate_votes/all_ballots_cast)*100
    cand_percentage.append(z)

winning_vote_total = max(votes_per_candidate)
winner = unique_candidate[votes_per_candidate.index(winning_vote_total)]

#Does this block create a dictionary????
#Don't we have to define Candidate_Name???

#if Candidate_Name not in Candidate: 
#if a Candidate_Name value doesn't appear in the Candidate list, append it - TO WHAT??
##AttributeError: 'dict' object has no attribute 'append'##
#        Candidate_Name.append(Candidate)
#       Candidate_Dictionary[Candidate] = 0 #initialize value to zero
#        Candidate_Dictionary[Candidate] +=1 #add up the number of times a Candidate_Name appear in loop

# Create a new txt file called Poll_Analysis in the Analysis folder to ouput analysis
#Set up variable for output file
output_file = os.path.join('Analysis/PyPoll_Analysis.txt','w') as out_file:
#open the output file                                           
with open ("output_file.txt,"w", newline = " "") as datafile
   out_file.write(
print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {str(all_ballots_cast)}")
print(f"-------------------------")
print(f"{str(candidate)}:" str{(candidate_percentage)}:.3f% str{(votes_per_candidate)}/)")
print(f"-------------------------")
print(f" Winner: str{unique_candidate[votes_per_candidate.index(winning_vote_total)]}")
print(f"(unique_candidate)")
print(f"-------------------------"))  
#Define election_results as string with formatting
        #election_results = (
        #Define voter_output as string with percentages calculated by candidate
        #Calculate percentage to three decimal places
        #voter_output = f"{Candidate}: {vote_percentage:.3f}% ({Votes})\n"

print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {str(all_ballots_cast)}")
print(f"-------------------------")
print(f"{str(candidate)}: str{(candidate_percentage)} str{(votes_per_candidate)})")
print(f"-------------------------")
print(f" Winner: str{unique_candidate[votes_per_candidate.index(winning_vote_total)]}")
print(f"(unique_candidate)")
print(f"-------------------------")      
        
#print the election results to the terminal
#print(election_results) #, end="")
#out_file.write(election_results)
       
#https://www.geeksforgeeks.org/python-merge-two-lists-into-list-of-tuples/
#def merge(BallotID,Candidate):
    #merged_list = [(BallotID[i],Candidate[i]) for i in range (0,len(BallotID))]
    #return merged_list

#https://www.tutorialspoint.com/How-I-can-convert-a-Python-Tuple-into-Dictionary
#inputTuple= merged_list
#Candidate_Dictionary = dict((x, y) for x, y in inputTuple)
#print("The resulting dictionary: ",Candidate_Dictionary )

#Counter(Candidate_Name).keys() # equals to list(set(words))
#Counter(Candidate_Name).values() # counts the elements' frequency
#count_dict = dict(Counter(Candidate_Name).items())
#print(count_dict)

# initializing the list
#candidate_list = [Candidate_Name]
#frequency = {}

# iterating over the list
#for item in candidate_list:
   # checking the element in dictionary
#   if item in frequency:
      # incrementing the count
#      frequency[item] += 1
#   else:
      # initializing the count
#      frequency[item] = 1

# printing the frequency
#print(frequency)
    #Candidate_Dictionary[Candidate] = 0 #initialize Candidate_Name values to zero in Candidate_Dictionary

#print(Candidate_Dictionary)
#for Candidate in csvreader: 
#    if Candidate not in Candidate_Dictionary:
#        Candidate.append(Candidate)
#        Candidate_Dictionary[Candidate] = 1 
#    else:
#        Candidate_Dictionary[Candidate] +1


#print the election results to the Poll_Analysis txt file out_file.write(election_results)
#Don't we need to define Votes?????
#Return key-value pairs in Candidate_Dictionary
#for Candidate_Name, Votes in Candidate_Dictionary.items():
    #Is this correct for what Votes means????   
    #    Votes = Candidate_Dictionary[Candidate_Name]
    #    print(Candidate_Name)
    #    print(Votes)   #Votes is number of times candidate's name appeared in above loop