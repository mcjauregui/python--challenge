#Import needed modules
import os
import csv
from collections import Counter
import sys

#Lists to store data
date = []
profitloss = []

# Construct file path using os.path.join()
budget_path = os.path.join("Resources","budget_data.csv")

#Open the CSV file
#Convert Profit/Loss values to integers when reading them from CSV 
#Use int(row[1]) to convert Profit/Loss values to integers
with open(budget_path, encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)  # Skip the header
    for row in csvreader:
        # Convert profit/loss value to integer
        profit_loss = int(row[1])
        # Append date and profit/loss to respective lists
        date.append(row[0])
        profitloss.append(profit_loss)
#print(profitloss)
#print(date)

#(1) The total number of months included in the dataset
#Count number of unique values in date list
unique_dates_count = len(set(date))
#print(unique_dates_count)

# (2) Find net total amount of "Profit/Losses" over entire period
net_total = sum(profitloss)
#print(net_total) 

# (3) Calculate changes in "Profit/Losses" over the entire period, and then the average of those changes
# https://www.geeksforgeeks.org/python-calculate-difference-between-adjacent-elements-in-given-list/
# a. Initialize list of month-to-month changes, diff_list
diff_list = []
# b. Calculate difference list
for i in range(1,len(profitloss)):  #start range at index 1, not index 0 to skip first value
     diff_list.append(profitloss[i] - profitloss[i-1])
#print(diff_list)  

#c. Sum up all the diff_list values
sum_all_diff = sum(diff_list)
#print(sum_all_diff)

# d. Find average of monthly changes
avg_monthly_diff = sum_all_diff/((unique_dates_count)-1)
#print(avg_monthly_diff)
        
#(4 and 5) Find the greatest increase and decrease in profits (date and amount) over the entire period
# a. Zip date list and diff_list list into list of tuples
# drop first value in dates list because date has one more value than diff_list
zipped_list = list(zip(date[1:], diff_list))  # Convert zipped_list to list

# b. Find the greatest increase and decrease in profits
max_diff = max(diff_list)
min_diff = min(diff_list)

# c. Find corresponding dates for max_diff and min_diff
# assistance provided by https://bootcampspot.instructure.com/courses/4981/external_tools/313
# Enumerate(diff_list) iterates over elements of diff_list along with their index positions
# for i, diff in enumerate(diff_list) unpacks index 'i' and value 'diff' from enumeration of diff_list
max_date = [date[i] for i, diff in enumerate(diff_list) if diff == max_diff]
min_date = [date[i] for i, diff in enumerate(diff_list) if diff == min_diff]
# date[i] retrieves date corresponding to index i where profit difference matches max_diff value
# List comprehension creates new lists (max_date and  min_date) containing all dates where profit difference equals max_diff or min_diff
#print("Greatest Increase in Profits:", max_date, max_diff)
#print("Greatest Decrease in Profits:", min_date, min_diff)

# Convert max_date and min_date lists to strings without brackets
max_date_str = '- '.join(max_date)
min_date_str = '- '.join(min_date)

#6. Print analysis to look like results given
# #Define financial_analysis as string with formatting
# #print the financial analysis to the terminal and to txt output file
financial_analysis = (
         f"\n\nFinancial Analysis\n"
         f"-------------------------\n"
         f"Total Months: {unique_dates_count}\n"
         f"Total: ${net_total}\n"
         f"Average Change: ${avg_monthly_diff:.2}\n"
         f"Greatest Increase in Profits: {max_date_str} (${max_diff})\n"
         f"Greatest Decrease in Profits: {min_date_str} (${min_diff})\n"
 )
print(financial_analysis)
output_file_path = "Analysis/financial_analysis.txt"
with open(output_file_path, 'w') as file:
     file.write(financial_analysis)