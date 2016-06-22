"""

  Created on 6/21/2016 by Ben

  pyjsviz - Example 5-1. Making a URL for the OECD API
  This makes use of the "requests" HTTP library and places
  OECD data as JSON in the SDMX format.

"""


import requests

OECD_ROOT_URL = 'http://stats.oecd.org/sdmx-json/data'


def make_OECD_request(dsname, dimensions, params=None, root_dir=OECD_ROOT_URL):
    """  Make a URL for the OECD-API and return a response  """

    #  shouldn't use mutable values, such as {}, for Py function defaults
    if not params:
        params = {}

    dim_args = ['+'.join(d) for d in dimensions]
    dim_str = '.'.join(dim_args)

    url= root_dir + '/' + dsname + '/' + dim_str + '/all'
    print('Requesting URL: ' + url)
    #  request's 'get' can take a parameter dictionary as 2nd argument
    return requests.get(url, params=params)

#  Grab economic data for the USA and Australia from 2009 - 2010:
response = make_OECD_request('QNA', (('USA', 'AUS'), ('GDP', 'B1_GE'), ('CUR', 'VOBARSA'), 'Q'),
                             {'startTime': '2009-Q1', 'endTime': '2010-Q1'})

#  Check the response and look at the dictionary keys:
if response.status_code == 200:
    json = response.json()
    json.keys()
    #  Out is ['header', 'dataSets', 'structure']
