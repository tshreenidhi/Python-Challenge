#importing the modules
import os
import csv

# Path to collect data from the Resources folder
budget_data_csv = os.path.join("Resources", "budget_data.csv")

#set the output of the text file
Output_path = "Shreenidhioutput.txt"

#Declare and initialise the variables needed
total_months = 0
total_revenue = 0
previous_revenue = 0
month_of_change = []
revenue_change = 0
revenue_average = 0
flag = True
months = []

#open and read the csv file and also reading it as a dictionary
with open(budget_data_csv) as csv_file:  
    #csv_reader = csv.DictReader(csv_file, delimiter=",")
    csv_reader = csv.reader(csv_file)
    #skip the header row
    header = next(csv_reader)
    
    #Find the total months in the dataset
    for row in csv_reader:

        #Count the total of months in the dataset
        total_months += 1

        months.append(row[0])       

        total_revenue = total_revenue + int(row[1])

        if flag == True:
            prev = int(row[1])
            flag = False
        

        change = int(row[1]) - prev 
        month_of_change.append(change)
        prev = int(row[1])
    
    #first month will have 0 value. so delete that value
    month_of_change.pop(0)
    months.pop(0)
    revenue_average = sum(month_of_change) / len(month_of_change)
  #Print the values to terminal    
    print(f'Total Months: {total_months} \n')
    print(f'Total Revenue: ${total_revenue} \n')
    print(f'Average Revenue Change ${revenue_average:.2f}\n')
    print(f'Greatest Increase in Revenue: {months[month_of_change.index(max(month_of_change))]} (${max(month_of_change)})')
    print(f'Greatest Decrease in Revenue: {months[month_of_change.index(min(month_of_change))]} (${min(month_of_change)})')
    
#write the output to a txt file
with open(Output_path, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("---------------------\n")
    file.write("Total Months: %d\n" % total_months)
    file.write("Total Revenue: $%d\n" % total_revenue)
    file.write(f'Average Revenue Change ${revenue_average:.2f}\n')
    file.write(f'Greatest Increase in Revenue: {months[month_of_change.index(max(month_of_change))]} (${max(month_of_change)})\n')
    file.write(f'Greatest Decrease in Revenue: {months[month_of_change.index(min(month_of_change))]} (${min(month_of_change)})')


    