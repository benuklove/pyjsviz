"""

  Created on 8/16/2016 by Ben

  benuklove@gmail.com
  
  Playing with Google Maps API Web Services for Python

"""

import googlemaps

gmaps = googlemaps.Client(key='AIzaSyBQRQEAGrUDyGZvzLGUD4nayxwYHhuL6xw')

# Geocode an address
geocode_result = gmaps.geocode('310 COLLEGE St Hughes AR 72348')

print(type(geocode_result))
print(geocode_result)
print(geocode_result[0]['geometry']['location']['lat'])
