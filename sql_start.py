"""

  Created on 6/25/2016 by Ben

  benuklove@gmail.com
  
  Create a (file-based) SQLite database using sqlalchemy.
  First creates a database engine.
  *** paused for now, learning more elsewhere ***

"""

from sqlalchemy import create_engine

#  echo argument outputs any SQL instruction generated by sqlalchemy
engine = create_engine('sqlite:///data/nobel_prize.db', echo=True)
