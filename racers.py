# Open the CSV file in read-only mode
file = open('racers.csv')

# Read the contents of the CSV file into one big string
file = file.read()

# Each line in the CSV is one racer, hence split by \n
# Creates a list where each item is an individual racer
racer_list = file.split('\n')

# Index 0 of the CSV is the key, hence we append everything from index 0 onwards to new list
new_racer_list = []
