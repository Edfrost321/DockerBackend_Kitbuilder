from pydantic import BaseModel

class Customer(BaseModel):
    acccode: str
    accname: str

    class Config:
        orm_mode = True

class Product(BaseModel):
    TAstockcode: str
    TAman_code: str
    TAdesc: str
    TAsubcatid: int

    width: float
    height: float
    sellprice: float

    class Config:
        orm_mode = True


class Panel(BaseModel):
    
    name: str
    description: str

    framecolor: str
    sheetcolor: str

    wattage: int
    vocstc: float

    width: float
    height: float
    sellprice: float

    class Config:
        orm_mode = True

class MountingComponent(BaseModel):

    rendercolor: str
    product_code: str
    mountingsystem: str

    class Config:
        orm_mode = True

class MountingSystemCreate(BaseModel):

    name: str

    class Config:
        orm_mode = True


class MountingSystem(MountingSystemCreate):
    name: str
    components: list[MountingComponent]

    class Config:
        orm_mode = True



