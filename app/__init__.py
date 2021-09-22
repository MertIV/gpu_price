from configobj import ConfigObj
from sqlalchemy import create_engine

config = ConfigObj('app/helper/config')

#general
# db = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)

#development
db = create_engine("sqlite+pysqlite:///app.db", echo=True, future=True)