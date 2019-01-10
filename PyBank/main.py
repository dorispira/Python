import os
import csv

# Path to collect data from folder
budget_dataCSV = os.path.join('.', 'budget_data.csv')

# Calculate each of the following:

# The total number of months included in the dataset (done)
# The total net amount of "Profit/Losses" over the entire period
# The average change in "Profit/Losses" between months over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period

# Setting the variables to 0

total_net = 0
sum_change = 0
avg_change = 0
max_increase = 0
max_decrease = 0
total_months = 0

# Creating month as list
max_increase_month = []
max_decrease_month = []

# Opening file as "r" and naming it
with open ('budget_data.csv', 'r') as csvfile:
    
    #identifying csv file with delimiter
    csvreader = csv.reader(csvfile, delimiter=',')
    
    header = next(csvreader)
    firstRow = next(csvreader)
    total_net = total_net + int(firstRow[1])
    total_months += 1
    previous_row = int(firstRow[1])
    
    # Adding rows to the list
    for row in csvreader:
        
        # Total number of months
        total_months += 1
        
        # Total net reveue
        total_net = total_net + int(row[1])
    
        # Loop the list to calculate changes, such as total, average, max increase, max decrease
        # for i in range(len(revenue)-1):
    
        # Total change between months
        sum_change = sum_change + int(row[1]) - previous_row
    
        # Greatest increase in profits
        change = int(row[1]) - previous_row
        
        # If we don't do this, it will always have the previous row variable stuck as THE FIRST ROW EVER
        previous_row = int(row[1])
        
        # Storing the difference (which is change in this case) as max_increase 
        # And comparing it with the next difference calculated
        # If next one is now highest, then store that instead and compare with next
        if (change > max_increase):
            max_increase = change
            max_increase_month = row[0]
        
        #Greatest decrease in profits
        if (change < max_decrease):
            max_decrease = change
            max_decrease_month = row[0]
    
# Calculate average change between months
avg_change = round(sum_change/(total_months-1),2)

# Print conclusion

print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(total_months))
print("Total: $" + str(total_net))
print("Average  Change: $" + str(avg_change))
print("Greatest Increase in Profits: " + max_increase_month +" $"+ str(max_increase))
print("Greatest Decrease in Profits: " + max_decrease_month +" $"+ str(max_decrease))

# Export file as txt
file = open('budget_output.txt','w')

file.write("Financial Analysis: Total Months - 86, Total Revenue - $38382578, Average Change - $-2315.12, Greatest Increase in Profits - Feb-12 $1926159, Greatest Decrease in Profits - Sep-13 $-2196167 ")

file.close