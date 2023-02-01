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

    truewidth: float
    trueheight: float
    sellprice: float

    class Config:
        orm_mode = True


class Panel(BaseModel):

    framecolor: str
    sheetcolor: str

    wattage: int
    vocstc: float

    class Config:
        orm_mode = True

class MountingComponent(BaseModel):

    rendercolor: str
    product_id: int
    mountingsystem: str

    class Config:
        orm_mode = True

class MountingSystem(BaseModel):

    name: str

    class Config:
        orm_mode = True


class MountingSystem(MountingSystem):
    name: str
    components: list[MountingComponent]

    class Config:
        orm_mode = True



