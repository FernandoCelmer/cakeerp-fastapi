from sqlalchemy.orm import Session

from fastapi import FastAPI, Depends, HTTPException

from typing import List

from app.models import Base
from app.crud import get_items, get_item, create_item
from app.schemas import SchemaItem, SchemaItemCreate
from app.database import get_db, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/status")
def status():
    return {"message": "Programa de Talentos 2022! CakeERP - NL Informática by Fernando Celmer"}


@app.get("/items", response_model=List[SchemaItem])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = get_items(db, skip=skip, limit=limit)   

    return items


@app.post("/items", response_model=SchemaItem, status_code=201)
def post_item(item: SchemaItemCreate, db: Session = Depends(get_db)):
    return create_item(db=db, item=item)    


@app.get("/items/{item_id}", response_model=SchemaItem)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = get_item(db=db, item_id=item_id)

    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    return db_item

