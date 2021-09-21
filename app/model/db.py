from sqlalchemy import text
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Float
from app import db

Base = declarative_base()

def execute(*args,**kwargs):
    with db.connect() as conn:
        result = conn.execute(*args,**kwargs)
        result = db.connect().execute()
        print(result.all())
    
    return result

class GPU(Base):
    __tablename__ = 'graphic_cards'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    incomes = relationship("Income",back_populates='graphic_card')
    hashrates = relationship("Hashrate", back_populates='graphic_card')
    deals = relationship("Market",back_populates='graphic_card')

    def __repr__(self):
        return "<Graphics Card(id='%s', name='%s'')>" % (
                            self.id, self.name)

class Income(Base):
    __tablename__ = 'income'
    id = Column(Integer, primary_key=True)
    gpu_id = Column(Integer,ForeignKey('graphic_cards.id'))
    pool = Column(String)
    amount = Column(Float)

    graphic_card = relationship("GPU",back_populates='incomes')

    def __repr__(self):
        return "<Daily Income(gpu_id='%s', pool='%s', amount='%s')>" % (
                            self.gpu_id, self.pool,self.amount)

class Hashrate(Base):
    __tablename__ = 'hashrate'
    id = Column(Integer, primary_key=True)
    gpu_id = Column(Integer,ForeignKey('graphic_cards.id'))
    coin = Column(String)
    hashrate = Column(Float)

    graphic_card = relationship("GPU",back_populates='hashrates')

    def __repr__(self):
        return "<Hashrate(gpu_id='%s', coin='%s', hashrate='%s')>" % (
                            self.gpu_id, self.coin,self.hashrate)

class Deal(Base):
    __tablename__ = 'deal'
    id = Column(Integer, primary_key=True)
    gpu_id = Column(Integer,ForeignKey('graphic_cards.id'))
    stock = Column(String)
    url = Column(String)
    price = Column(Float)

    graphic_card = relationship("GPU",back_populates='deals')

    def __repr__(self):
        return "<Deal(gpu_id='%s',stock='%s' ,url='%s', price='%s')>" % (
                            self.gpu_id,self.stock, self.url,self.price)


Base.metadata.create_all(db)