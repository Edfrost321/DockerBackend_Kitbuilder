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

    id = Column(Integer, primary_key=True, index=True)
    TAstockcode = Column(VARCHAR(30), unique=True)
    TAman_code = Column(VARCHAR(30), unique=True, index=True)
    TAdesc = Column(VARCHAR(250))
    TAsubcatid = Column(Integer)

    truewidth = Column(Float)
    trueheight = Column(Float)
    sellprice = Column(Numeric(2))

    panel = relationship("Panel", uselist=False, backref="product")
    mountingcomponent = relationship("MountingComponent", uselist=False, backref="product")
    

class Panel(Base):
    __tablename__ = "panel"

    id = Column(Integer, primary_key=True, index=True)

    framecolor = Column(String)
    sheetcolor = Column(String)

    wattage = Column(Integer)
    vocstc = Column(Float)

    product_id = Column(Integer, ForeignKey("product.id"))



class MountingSystem(Base):
    __tablename__ = "mountingsystem"

    name = Column(VARCHAR(20), primary_key=True, index=True)
    components = relationship("MountingComponent")

class MountingComponent(Base):
    __tablename__ = "mountingcomponent"

    id = Column(Integer, primary_key=True, index=True)

    rendercolor = Column(String)

    mountingsystem = Column(String, ForeignKey("mountingsystem.name"))
    product_id = Column(Integer, ForeignKey("product.id"))


