"""

  Created on 6/22/2016 by Ben


"""


import requests
import pprint

REST_EU_ROOT_URL = "http://restcountries.eu/rest/v1"

#  Function to access REST-countries API
def REST_country_request(field='all', name=None, params=None):

    #  Specify user-agent; some sites will reject request otherwise
    headers = {'User-Agent': 'Chrome/51.0.2704.103'}

    #  shouldn't use mutable values, such as {}, for Py function defaults
    if not params:
        params = {}

    if field == 'all':
        return requests.get(REST_EU_ROOT_URL + '/all')

    url = '%s/%s/%s'%(REST_EU_ROOT_URL, field, name)
    print('Requesting URL: ' + url)
    respon = requests.get(url, params=params, headers=headers)

    #  Make sure status code is OK
    if not respon.status_code == 200:
        raise Exception('Request failed with status code ' + str(respon.status_code))

    return respon

#  Check all countries that use US-dollar as currency:
response = REST_country_request('currency', 'usd')
if response.status_code == 200:
    response.json()

#  Pretty-print json
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(response.json())
