#Check current working directory
import os
print(os.getcwd())

# Check if the file exists in the current working directory
file_name = 'budget_data.csv'
file_exists = os.path.exists(file_name)

if file_exists:
    print(f"The file {file_name} exists in the current working directory.")
else:
    print(f"The file {file_name} does not exist in the current working directory.")

import os

# Get a list of all files in the current working directory
files_in_directory = os.listdir()

# Print the list of files
print("Files in the current working directory:")
for file in files_in_directory:
    print(file)



#Import needed modules
import os
import csv
from collections import Counter
import sys

#Lists to store data
Date = []
ProfitLoss = []

# Construct the file path using os.path.join()
budget_csv = os.path.join("PyBank", "Resources", "budget_data.csv")

#Instructions for reading CSV module
budget_csv = os.path.join("PyBank","Resources","budget_data.csv")

#Open the CSV file
#Convert Profit/Loss values to integers when reading them from CSV 
#Use int(row[1]) to convert Profit/Loss values to integers
with open('budget_data.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)  # Skip the header
    for row in csvreader:
        # Convert the profit/loss value to an integer
        profit_loss = int(row[1])
        # Append the date and profit/loss to the respective lists
        Date.append(row[0])
        ProfitLoss.append(profit_loss)
   
#(1) Count the number of unique values in Date list
unique_dates_count = len(set(Date))
print("Number of unique values months in the dataset:", unique_dates_count)

#(2) Find the net total amount of "Profit/Losses" over the entire period
net_total = sum(ProfitLoss)
print(net_total)

#(3) The changes in "Profit/Losses" over the entire period, and then the average of those changes
#https://www.geeksforgeeks.org/python-calculate-difference-between-adjacent-elements-in-given-list/
#a. Initializing list of month-to-month changes
diff_list = []
#b. Calculating difference list
for i in range(1,len(ProfitLoss)):
    diff_list.append(ProfitLoss[i] - ProfitLoss[i-1])
sum_period_changes = sum(diff_list)
print(sum_period_changes)

#c. Find average of mothly changes
#avg_monthly_diff = sum_period_changes/unique_dates_count
avg_monthly_diff = sum_period_changes/((unique_dates_count)-1)

print(avg_monthly_diff)
        
#(4) Find the greatest increase in profits (date and amount) over the entire period
# a. Combine diff_list and dates into list of tuples
diff_date = list(zip(Date, diff_list))
print(diff_date)

greatest_increase = max(diff_list)
print(greatest_increase)
increase_date = diff_list.index(max(diff_list))
print(increase_date)

# b. Define custom function to extract value from tuple
# https://bootcampspot.instructure.com/courses/4981/external_tools/313
#def get_difflist_value(tuple_item):
#    return tuple_item[1]  #Extracts the diff_list value from each tuple

#c. Find tuple with maximum diff_list value using custom function
#max_tuple = max(diff_date, key=get_dollar_value) #specifying max of diff_list value

#d. Extract date and diff_list value from tuple with maximum value (based on diff_list value)
#max_date = max_tuple[0]
#max_value = max_tuple[1]

#print("The greatest increase in profits is:", max_value)
#print("The corresponding date is:", max_date)

#(5) Find the greatest decrease in profits (date and amount) over the entire period
#a. Find tuple with minimum diff_list value using custom function
#min_tuple = min(diff_date, key=get_dollar_value) #specifying max of diff_list value

#b. Extract date and diff_list value from tuple with maximum value (based on diff_list value)
#min_date = min_tuple[0]
#min_value = min_tuple[1]

#print("The greatest decrease in profits is:", min_value)
#print("The corresponding date is:", min_date)

greatest_decrease = (min(diff_list))
print(greatest_decrease)
decrease_date = diff_list.index(min(diff_list))
print(decrease_date)

print("The greatest decrease in profits is:", greatest_decrease)
print("The corresponding date is:", decrease_date)

#6. Print analysis to look like results given
#Define financial_analysis as string with formatting
#print the financial analysis to the terminal and to txt  output file
financial_analysis = (
        f"\n\nFinancial Analysis\n"
        f"-------------------------\n"
        f"Total Months: {unique_dates_count}\n"
        f"Total: ${net_total}\n"
        f"Average Chang: ${avg_monthly_diff:.2}\n"
        f"Greatest Increase in Profits: {increase_date} (${greatest_increase})\n"
        f"Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})\n"
)
print(financial_analysis)
output_file_path = "python-challenge/PyBank/Analysis/financial_analysis.txt"
with open(output_file_path, 'w') as file:
    file.write(financial_analysis)

#Dates code provided by Melissa Krachmer
#https://stackoverflow.com/questions/53041365/python-maximum-difference-between-elements-in-a-list
# 4) The greatest increase in profits (date and amount) over the entire period
#greatest_increase = (max[diff_list])
#print(greatest_increase)
#increase_date = date[diff_list.index(greatest_increase)]
#print(increase_date)

#5) The greatest decrease in profits (date and amount) over the entire period. 
#greatest_decrease = (min[diff_list])
#print(greatest_decrease)
#decrease_date = date[diff_list.index(greatest_decrease)]
#print(decrease_date)