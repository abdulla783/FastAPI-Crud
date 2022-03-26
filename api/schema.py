from pydantic import BaseModel
from typing import List


''' Model Schema Using Pydantic '''


class Address(BaseModel):
    id: int
    address: str
    longitude: str
    latitude: str
    is_published: bool = False  # Providing a default value False
    # created: datetime = datetime.utcnow()
    # updated: datetime = datetime.utcnow()

    # class Config:
    #     orm_mode = True

class AddressIn(BaseModel):
    address: str
    longitude: str
    latitude: str
    is_published: bool = False
    # Providing a default value False
    # created: datetime = datetime.utcnow()
    # updated: datetime = datetime.utcnow()

    # class Config:
    #     orm_mode = True