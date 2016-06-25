"""

  Created on 6/25/2016 by Ben

  benuklove@gmail.com
  
  Reads json with 'load' method; pretty prints

"""

import json
import pprint

with open('data/nobel_winners.json') as f:
    nobel_winners = json.load(f)

#  Pretty-print json
pp = pprint.PrettyPrinter()
pp.pprint(nobel_winners)
