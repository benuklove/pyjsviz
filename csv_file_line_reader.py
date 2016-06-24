"""

  Created on 6/23/2016 by Ben

  Reads file - in this case, the one listed - and
  prints csv line by line as lists

"""


import csv

with open('data/nobel_winners.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
