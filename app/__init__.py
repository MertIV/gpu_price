from configobj import ConfigObj
from sqlalchemy import create_engine

config = ConfigObj('app/helper/confg')
db = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)

