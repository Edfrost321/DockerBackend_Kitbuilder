from sqlalchemy import Column, DateTime, TIMESTAMP ,ForeignKey, Integer, String, Float, Numeric, VARCHAR, BOOLEAN
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


Base = declarative_base()



class Customer(Base):
    __tablename__ = "customer"

    acccode = Column(String, primary_key=True, index=True)
    accname = Column(String)

class User(Base):
    __tablename__ = "user"

    acccode = Column(
        String,
        ForeignKey("customer.acccode"),
        index=True,
        nullable=True
    )

    email = Column(String, nullable=False, primary_key=True)
    password = Column(String, nullable=False)
    isStaff = Column(BOOLEAN, server_default='FALSE')
    createdat = Column(TIMESTAMP(timezone=True),
                            nullable=False, server_default=text('now()'))


class Product(Base):
    __tablename__ = "product"

    TAstockcode = Column(VARCHAR(30), unique=True)
    TAman_code = Column(VARCHAR(30), primary_key=True, unique=True, index=True)
    TAdesc = Column(VARCHAR(250))
    TAsubcatid = Column(Integer)

    width = Column(Float)
    height = Column(Float)
    sellprice = Column(Float)

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
    product_code = Column(VARCHAR(30), ForeignKey("product.TAman_code"), primary_key=True, index=True)


