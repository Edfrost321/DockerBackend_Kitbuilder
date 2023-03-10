from sqlalchemy.orm import Session

import models, schema

def get_customers(db: Session, skip: int = 0, limit: int=100):
    return db.query(models.Customer).offset(skip).limit(limit).all();

def get_panels(db: Session, skip: int = 0, limit: int=100):
    return db.query(models.Panel).offset(skip).limit(limit).all();

def get_products(db: Session, skip: int = 0, limit: int=100):
    return db.query(models.Product).offset(skip).limit(limit).all();

def get_mounting(db: Session, skip: int = 0, limit: int=100):
    return db.query(models.MountingComponent).offset(skip).limit(limit).all();