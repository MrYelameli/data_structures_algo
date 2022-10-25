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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

text_outgoing = []
text_incoming = []
for i, j, _ in texts:
    text_outgoing.append(i)
    text_incoming.append(j)

call_receive = []
call_outgoing = []
for i, j, _, _ in calls:
    call_outgoing.append(i)
    call_receive.append(j)

unique = list(set().union(set(text_outgoing), set(text_incoming), set(call_receive)))
telemarketing_numbers = []
for i in call_outgoing:
    if i not in unique:
        telemarketing_numbers.append(i)

telemarketing_numbers_ = list(sorted(set(telemarketing_numbers)))
print("These numbers could be telemarketers:")
for t in telemarketing_numbers_:
    print(t)