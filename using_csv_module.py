"""

  Created on 6/23/2016 by Ben

  Does same thing as passing_data.py but with Python's csv module
  (Writes a csv file from a python list of dictionaries)

"""


import csv

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

with open('data/nobel_winners.csv', 'w', newline='') as f:
    fieldnames = list(nobel_winners[0].keys())
    fieldnames.sort()
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for w in nobel_winners:
        writer.writerow(w)
