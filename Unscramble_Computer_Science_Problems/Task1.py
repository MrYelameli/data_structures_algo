"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

unique_numbers=set()
[unique_numbers.update([i[0],i[1]]) for i in texts] #(O(n))
[unique_numbers.update([i[0],i[1]]) for i in calls] #(O(n)
print(len(unique_numbers)) #(0(1))
