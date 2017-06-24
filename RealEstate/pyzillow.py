"""

  Created on 1/21/2017 by Ben

  benuklove@gmail.com
  
  

"""

import pandas as pd

# Read in relevant data
ar = pd.read_csv('statewide.csv', low_memory=False)
address_cols = ['NUMBER', 'STREET', 'CITY', 'REGION', 'POSTCODE']
ar_select = ar[address_cols]

# Select only Bella Vista addresses
bv = ar_select.loc[ar_select['CITY'] == 'Bella Vista']

# Check for NaN (and print total)
print(bv.isnull().sum().sum())

print(bv)
