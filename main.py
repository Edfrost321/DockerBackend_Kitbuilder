import os
from dotenv import load_dotenv
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_sqlalchemy import DBSessionMiddleware, db

from schema import Customer, Product, Panel, MountingSystem, MountingComponent
from models import Product as ModelProduct
from models import Customer as ModelCustomer
import crud

load_dotenv(".env")

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])


# CORS setup
origins = [
    "http://127.0.0.1:5500",
    ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/add-customer/", response_model=Customer)
async def add_customer(customer: Customer):
    db_customer = ModelCustomer(
        acccode = customer.acccode,
        accname = customer.accname
    )
    db.session.add(db_customer)
    db.session.commit()
    return db_customer


@app.post("/get_customers/", response_model=list[Customer])
async def get_all_customers():
    customers = crud.get_customers(db.session)
    return customers



@app.post("/add-product/", response_model=Product)
async def add_product(product: Product):
    db_product = ModelProduct(
        TAstockcode=product.TAstockcode,
        TAman_code=product.TAman_code,
        TAdesc=product.TAdesc,
        TAsubcatid=product.TAsubcatid,

        truewidth=product.truewidth,
        trueheight=product.trueheight,
        sellprice=product.sellprice
    )
    db.session.add(db_product)
    db.session.commit()
    return db_product

# @app.get("/get-panel/", response_model=Panel)