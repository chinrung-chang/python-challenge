import csv


# Total number of months
count = 0
# Net total number profit/losses
sum = 0
# Total dollar amount change
totalChange = 0
# greatest increase dollar change
greatestIncrease = 0
# greatest decrease dollar change
greatestDecrease = 0
# greatest increase dollar change date
greatestIncreaseDate = ''
# greatest decrease dollar change date
greatestDecreaseDate = ''

# read csv file
csvpath = './Resources/budget_data.csv'
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
   
    # Profit/Losses
    budget = 0
    # Dollar amount change by month
    change = 0    
    # Read each row of data after the header
    for row in csvreader:
        # row count
        count = count + 1        
        if (count > 1):            
            # the dollar amount change start from second row of data
            change = int(row[1]) - budget            
        # store dollar amount of each date
        budget = int(row[1])        
        # store total dollar amount
        sum = sum + budget
        # store total dollar amount change
        totalChange = totalChange + change
        # store greatest increase
        if (greatestIncrease < change):
            greatestIncreaseDate = row[0]
            greatestIncrease = change
        # store greatest decrease
        if ( greatestDecrease > change):
            greatestDecreaseDate = row[0]
            greatestDecrease = change

#average of the change
average = round(totalChange/(count-1), 2)

#put the output by lines in a list
outputLines = [
    "Financial Analysis",
    "----------------------------",
    f"Total Months: {count}",
    f"Total: {sum}",
    f"Average Change: ${average}",
    f"Greatest Increase in Profits: {greatestIncreaseDate} (${greatestIncrease})",
    f"Greatest Decrease in Profits: {greatestDecreaseDate} (${greatestDecrease})"]

#print the list
for line in outputLines:
    print(line + "\n")

# output the list to output.txt in sub folder analysis
outputPath = './analysis/output.txt'
with open(outputPath, 'w') as f:
    for line in outputLines:
        f.write(line + "\n")    
