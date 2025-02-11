from pydantic import BaseModel

class RoomBase(BaseModel):
    name: str
    description: str
    price: float
    is_available: bool

class RoomCreate(RoomBase):
    pass

class RoomResponse(RoomBase):
    id: int

    class Config:
        orm_mode = True
