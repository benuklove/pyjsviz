"""

  Created on 6/25/2016 by Ben

  benuklove@gmail.com
  
  Custom encoder provided to the json.dumps method as a cls argument.
  Encoder is applied to each object in your data, converting to ISO-
  format string.
  Prints current date and time.
  'strptime' method, part of datetime.datetime package could also be used

"""

import datetime
from dateutil import parser
import json


#  Subclass a JSONEncoder in order to create a customized date-handling one
class JSONDateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        #  Test for a datetime object, if true returns ISO format,
        #  e.g. 2015-09-13T10:25:52.586792
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()
        else:
            return json.JSONEncoder.default(self, obj)


def dumps(obj):
    #  Uses cls argument to set our custom date-encoder
    return json.dumps(obj, cls=JSONDateTimeEncoder)

now_str = dumps({'time': datetime.datetime.now()})
print(now_str)
