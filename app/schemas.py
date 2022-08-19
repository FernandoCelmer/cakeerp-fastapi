from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class SchemaItemBase(BaseModel):
    title: str
    description: Optional[str] = None
    created_date: datetime = None


class SchemaItemCreate(SchemaItemBase):
    pass


class SchemaItem(SchemaItemBase):
    id: int

    class Config:
        orm_mode = True

