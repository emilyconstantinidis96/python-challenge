import os
import csv

# Path to collect budget data 
budgetdata_csv = 'budget_data1.csv'

# variables
mcount = 0; total = 0; PreValue = 0; DiffMax = 0; DiffMin = 0

with open(budgetdata_csv, newline="") as csvfile:
    csv_reader = csv.reader(csvfile,delimiter = ",")
    csv_header = next(csv_reader)


print(f'Financial Analysis' + '\n')

print(f'------------------------'+'\n') 

for i in csv_reader:
    month = i[0]
    amount = i[1]
    iamount = int(amount)
    Diff = iamount - PreValue

# track greatest increase in profits
if DiffMax < Diff:
    DiffMax = Diff
    DiffMaxDate = month

# track greatest decrease in profits
if DiffMin > Diff:
    DiffMin = Diff
    DiffMinDate = month

PreValue = iamount

# total months
mcount = mcount + 1
total+= int(amount)

print(f'Total Months: {mcount}')

print(f'Total: $ {total}')

print(f'Greatest Increase in Profits: {DiffMaxDate} : (${DiffMax})')

print(f'Greatest Decrease in Profits: {DiffMinDate} : (${DiffMin})')