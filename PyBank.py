#Import dependencies
import os
import csv

#Define the relative path to csv
csvpath = os.path.join('Resources', 'budget_data.csv')

#initalizing variables
number_months = 0
total_pl = 0
total_profit_change = 0
greatest_profit = 0
greatest_loss = 0

#opening the csv
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    #print the header
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:

        if number_months == 0:
            change_profits = 0
        else:
            change_profits = int(row[1]) - prev_month
            total_profit_change = change_profits + total_profit_change 

        if change_profits > greatest_profit:
            greatest_profit = change_profits
            greatest_month = row[0]
        elif change_profits < greatest_loss:
            greatest_loss = change_profits
            lowest_month = row[0]
    
        number_months = number_months + 1
        total_pl = total_pl + int(row[1])
      
        month = row[0]
        profits_losses = int(row[1])


        prev_month = int(row[1])
            
avg_profit_change = total_profit_change/(number_months - 1)    
print(number_months)
print(total_pl)
print(avg_profit_change)
print(greatest_profit)
print(greatest_month)
print(greatest_loss)
print(lowest_month)

output = f"""
Financial Analysis
----------------------
Total Months: {number_months}
Total: ${total_pl}
Average Change: ${avg_profit_change} 
Greatest Increase in Profits: ${greatest_profit}({greatest_month})
Greatest Decrease in Profits: ${greatest_loss}({lowest_month})

"""
print(output)




