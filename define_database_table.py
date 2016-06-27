"""

  Created on 6/26/2016 by Ben

  benuklove@gmail.com
  
  Database table configuration
  *** paused for now, learning more elsewhere ***

"""

from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Winner(Base):
    __tablename__ = 'winners'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    category = Column(String)
    year = Column(Integer)
    nationality = Column(String)
    sex = Column(Enum('male', 'female'))

    def __repr__(self):
        return "<Winner(name='%s', category='%s', year='%s')>"\
            %(self.name, self.category, self.year)

# Base.metadata.create_all(engine)
# INFO:sqlalchemy.engine.base.Engine SELECT CAST('test plain returns' AS VARCHAR(60)) AS anon_1
