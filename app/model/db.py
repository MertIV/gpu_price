from sqlalchemy import Column, Integer, String, MetaData, DateTime
from sqlalchemy.orm import declarative_base, relationship, Session
from sqlalchemy.sql import func
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Float
from app import db
import contextlib

Base = declarative_base()
meta = MetaData(db)

def execute(*args,**kwargs):
    with db.connect() as conn:
        result = conn.execute(*args,**kwargs)
        result = db.connect().execute()
        print(result.all())
    
    return result

def create_session():
    session = Session(db, future=True)
    return session

def truncate_tables():
    with contextlib.closing(db.connect()) as con:
        trans = con.begin()
        for table in reversed(Base.metadata.sorted_tables):
            con.execute(table.delete())
        trans.commit()

def drop_tables():
    Base.metadata.drop_all(db)

class GPU(Base):
    __tablename__ ='graphic_cards'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    incomes = relationship("Income",back_populates='graphic_card')
    hashrates = relationship("Hashrate", back_populates='graphic_card')
    deals = relationship("Deal",back_populates='graphic_card')

    def __repr__(self):
        return "<Graphics Card(id='%s', name='%s'')>" % (
                            self.id, self.name)

class Income(Base):
    __tablename__ = 'income'
    id = Column(Integer, primary_key=True)
    gpu_id = Column(Integer,ForeignKey('graphic_cards.id'),nullable=False)
    pool = Column(String)
    amount = Column(Float)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())

    graphic_card = relationship("GPU",back_populates='incomes')

    def __repr__(self):
        return "<Daily Income(gpu_id='%s', pool='%s', amount='%s')>" % (
                            self.gpu_id, self.pool,self.amount)

class Hashrate(Base):
    __tablename__ = 'hashrate'
    id = Column(Integer, primary_key=True)
    gpu_id = Column(Integer,ForeignKey('graphic_cards.id'),nullable=False)
    coin = Column(String)
    hashrate = Column(Float)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())

    graphic_card = relationship("GPU",back_populates='hashrates')

    def __repr__(self):
        return "<Hashrate(gpu_id='%s', coin='%s', hashrate='%s')>" % (
                            self.gpu_id, self.coin,self.hashrate)

class Deal(Base):
    __tablename__ = 'deal'
    id = Column(Integer, primary_key=True)
    gpu_id = Column(Integer,ForeignKey('graphic_cards.id'),nullable=False)
    stock = Column(String)
    url = Column(String)
    price = Column(Float)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())

    graphic_card = relationship("GPU",back_populates='deals')

    def __repr__(self):
        return "<Deal(gpu_id='%s',stock='%s' ,url='%s', price='%s')>" % (
                            self.gpu_id,self.stock, self.url,self.price)


# Base.metadata.create_all(db)