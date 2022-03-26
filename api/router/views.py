from fastapi import APIRouter, status, FastAPI, HTTPException
# from typing import List,Optional
# from databases import Database
from database import engine, SessionLocal, Base, database
from model import address_

from schema import AddressIn, Address
from typing import List

router = APIRouter()
app = FastAPI()


@router.on_event("startup")
async def startup():
    await database.connect()


@router.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@router.get("/address/", response_model=List[Address], status_code=status.HTTP_200_OK)
async def read_notes(skip: int = 0, take: int = 20):
    query = address_.select().offset(skip).limit(take)
    return await database.fetch_all(query)


@router.get("/address/{address_id}/", response_model=Address, status_code=status.HTTP_200_OK)
async def read_notes(address_id: int):
    query = address_.select().where(address_.c.id == address_id)

    return await database.fetch_one(query)


@router.post("/address/", response_model=Address, status_code=status.HTTP_201_CREATED)
async def create_note(data: AddressIn):
    query = address_.insert().values(address=data.address, latitude=data.latitude, longitude=data.longitude,
                                     is_published=data.is_published)
    last_record_id = await database.execute(query)
    return {**data.dict(), "id": last_record_id}


@router.put("/address/{address_id}/", response_model=AddressIn, status_code=status.HTTP_200_OK)
async def update_note(address_id: int, payload: AddressIn):
    query = address_.update().where(address_.c.id == address_id).values(address=payload.address,
                                                                        latitude=payload.latitude,
                                                                        longitude=payload.longitude,
                                                                        is_published=payload.is_published)
    last_record_id_ = await database.execute(query)
    print("last_record_id_", last_record_id_)
    # return {"ff"}
    return {**payload.dict(), "id": address_id}


@router.delete("/address/{address_id}/", status_code=status.HTTP_200_OK)
async def delete_note(address_id: int):
    query = address_.delete().where(address_.c.id == address_id)
    await database.execute(query)
    return {"message": f"Note with id {address_id}:deleted successfully!"}





