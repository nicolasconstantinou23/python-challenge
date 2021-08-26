# Import modules
import os
import csv

# Define variables, and lists to store data
total_months = 0
net_amount = 0
monthly_change = []
month_count = []
greatest_increase = 0
greatest_increase_month = 0
greatest_decrease = 0
greatest_decrease_month = 0

# Set path for file
csvpath = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')

# Open the CSV
with open(csvpath, newline='') as csvfile:
    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row first
    csv_header = next(csvreader)
    row = next(csvreader)
    
    # Calculate the total number of months, net total amount of "Profit/Losses" and define variables for rows
    previous_row = int(row[1])
    total_months += 1
    net_amount += int(row[1])
    greatest_increase = int(row[1])
    greatest_increase_month = row[0]
    
    # Read through each row of data after the header
    for row in csvreader:
        
        # Calculate the total number of months in the dataset
        total_months += 1
        # Calculate the net amount of "Profit/Losses" over the entire period
        net_amount += int(row[1])

        # Calculate the change between the current month and the previous month
        revenue_change = int(row[1]) - previous_row
        monthly_change.append(revenue_change)
        previous_row = int(row[1])
        month_count.append(row[0])
        
        # Calculate the greatest increase in profits (amount) over the entire period
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_increase_month = row[0]
            
        # Calculate the greatest decrease in losses (amount) over the entire period
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_decrease_month = row[0]  
        
    # Calculate the average of the changes in "Profit/Losses" (amount) over the entire period
    average_change = sum(monthly_change)/ len(monthly_change)
    
    # Calculate the greatest increase in profits (date) and the greatest decrease in losses (date) over the entire period
    highest = max(monthly_change)
    lowest = min(monthly_change)

# Print Analysis
print(f"Financial Analysis")
print(f"---------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_amount}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${highest})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${lowest})")

# Specify the file to write to
output_file = os.path.join('..', 'PyBank', 'Analysis', 'results.txt')

# Open the file using "write" mode and specify the variable to hold the contents
with open(output_file, 'w',) as txtfile:

# Write output to txtfile
    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${net_amount}\n")
    txtfile.write(f"Average Change: ${average_change:.2f}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_increase_month} (${highest})\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${lowest})\n")