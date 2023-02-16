import os
from dotenv import load_dotenv
import uvicorn
from fastapi import FastAPI, Request, Response, File, UploadFile, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi_sqlalchemy import DBSessionMiddleware, db
from io import BytesIO


from schema import Customer, Product, Panel, MountingSystemCreate, MountingSystem, MountingComponent
from models import Product as ModelProduct
from models import Panel as ModelPanel
from models import Customer as ModelCustomer
from models import MountingSystem as ModelMsys
import crud

import pandas as pd

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


@app.get("/get_customers/", response_model=list[Customer])
async def get_all_customers():
    customers = crud.get_customers(db.session)
    return customers

@app.get("/get_panels/", response_model=list[Panel])
async def get_all_panels():
    panels = crud.get_panels(db.session)
    return panels

@app.get("/get_products/", response_model=list[Product])
async def get_all_products():
    products = crud.get_products(db.session)
    return products

@app.get("/get_mounting/", response_model=list[MountingComponent])
async def get_all_mounting():
    products = crud.get_mounting(db.session)
    return products

@app.post("/add-product/", response_model=Product)
async def add_product(product: Product):
    db_product = ModelProduct(
        TAstockcode=product.TAstockcode,
        TAman_code=product.TAman_code,
        TAdesc=product.TAdesc,
        TAsubcatid=product.TAsubcatid,

        width=product.width,
        height=product.height,
        sellprice=product.sellprice
    )
    db.session.add(db_product)
    db.session.commit()
    return db_product


# Mounting
@app.post("/add-mountingsys/", response_model=MountingSystemCreate)
async def add_mountingsys(mountingsys: MountingSystemCreate):
    db_msys = ModelMsys(
        name=mountingsys.name
    )
    db.session.add(db_msys)
    db.session.commit()
    return db_msys
