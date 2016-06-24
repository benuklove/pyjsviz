"""

  Created on 6/23/2016 by Ben

  Creates a CSV file from a Python list of dictionaries, Example 3-1

"""


nobel_winners = [
    {'category': 'Physics',
        'name': 'Albert Einstein',
        'nationality': 'Swiss',
        'sex': 'male',
        'year': 1921},
    {'category': 'Physics',
        'name': 'Paul Dirac',
        'nationality': 'British',
        'sex': 'male',
        'year': 1933},
    {'category': 'Chemistry',
        'name': 'Marie Curie',
        'nationality': 'Polish',
        'sex': 'female',
        'year': 1911}
]

f = open('data/nobel_winners.csv', 'w')

#  Get data columns from keys of the first object, i.e. "category, name, ..."
#  Two lines below work same as next two
cols = list(nobel_winners[0].keys())
cols.sort()

#  Guarantee the file is closed on leaving the block or if any exceptions occur
with open('data/nobel_winners.csv', 'w') as f:
    #  join creates a concatenated string from a list of strings - cols, joined by initial string
    f.write(','.join(cols) + '\n')

    for o in nobel_winners:
        #  Creates a list using the column keys to the objects in nobel_winners
        row = [str(o[col]) for col in cols]
        f.write(','.join(row) + '\n')

with open('data/nobel_winners.csv') as f:
    for line in f.readlines():
        print(line)
