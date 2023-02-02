from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float, Numeric, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


Base = declarative_base()

class Customer(Base):
    __tablename__ = "customer"

    acccode = Column(String, primary_key=True, index=True)
    accname = Column(String)


class Product(Base):
    __tablename__ = "product"

    TAstockcode = Column(VARCHAR(30), unique=True)
    TAman_code = Column(VARCHAR(30), primary_key=True, unique=True, index=True)
    TAdesc = Column(VARCHAR(250))
    TAsubcatid = Column(Integer)

    width = Column(Float)
    height = Column(Float)
    sellprice = Column(Numeric(2))

    mountingcomponent = relationship("MountingComponent", uselist=False, backref="product")
    

class Panel(Base):
    # Panels aren't linked to a product because they're not on TradeAccounts
    # so importing the man_code won't work
    __tablename__ = "panel"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)

    framecolor = Column(String)
    sheetcolor = Column(String)

    wattage = Column(Integer, index=True)
    vocstc = Column(Float)

    width = Column(Float)
    height = Column(Float)
    sellprice = Column(Float)



class MountingSystem(Base):
    __tablename__ = "mountingsystem"

    name = Column(VARCHAR(20), primary_key=True, index=True)
    components = relationship("MountingComponent")

class MountingComponent(Base):
    __tablename__ = "mountingcomponent"

    rendercolor = Column(String)

    mountingsystem = Column(String, ForeignKey("mountingsystem.name"))
    product_code = Column(VARCHAR(30), ForeignKey("product.TAman_code"), primary_key=True)


