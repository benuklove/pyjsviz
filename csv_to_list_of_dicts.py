"""

  Created on 6/24/2016 by Ben

  Takes our .csv and converts it to a list of dictionaries
  Then pretty prints them

"""


import csv
import pprint

with open('data/nobel_winners.csv') as f:
    reader = csv.DictReader(f)
    nobel_winners = list(reader)

#  Cast 'year' attribute from string to integer
for w in nobel_winners:
    w['year'] = int(w['year'])

#  Pretty-print dictionaries
pp = pprint.PrettyPrinter()
pp.pprint(nobel_winners)
