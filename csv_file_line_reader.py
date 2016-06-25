"""

  Created on 6/23/2016 by Ben

  Reads file - in this case, the one listed - and
  prints csv line by line as lists

"""


import csv

#  Note that numbers are read as strings - and output as strings
#  If you want this to change, you could add line 19 below:
with open('data/nobel_winners.csv') as f:
    reader = csv.reader(f)
    print(next(reader))
    for row in reader:
        row[4] = int(row[4])
        print(row)
