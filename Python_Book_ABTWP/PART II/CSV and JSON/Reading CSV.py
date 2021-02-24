import csv

file = open('addresses.csv')
file_reader = csv.reader(file)

# ss  = list(file_reader) #converting to list
for row in file_reader:
     print(row)


# print(ss)

