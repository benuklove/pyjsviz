"""

  Created on 8/12/2016 by Ben

  benuklove@gmail.com
  
  Testing the geopy 1.11.0 package

"""

from geopy.geocoders import Nominatim
geolocator = Nominatim()
location = geolocator.geocode("175 5th Avenue NYC")
print(location.address)
print(location.latitude, location.longitude)
