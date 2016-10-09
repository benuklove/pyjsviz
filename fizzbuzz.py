"""

  Created on 8/12/2016 by Ben

  benuklove@gmail.com
  
  LOL did this for a udacity readiness test

"""


def fizzbuzz(intlist):
    newlist = []
    for item in intlist:
        if item % 3 == 0 and item % 5 == 0:
            newlist.append("FizzBuzz")
        elif item % 3 == 0:
            newlist.append("Fizz")
        elif item % 5 == 0:
            newlist.append("Buzz")
        else:
            newlist.append(item)
    return newlist

mylist = [2, 15, 7, 36, 20, 13, 9]
result = fizzbuzz(mylist)
print(result)
