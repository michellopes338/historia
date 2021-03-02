from pydantic import BaseModel


class PointsBase(BaseModel):
    id: int
    points: int


class PointsUpdate(BaseModel):
    pass


class PointsIn(BaseModel):
    points: int


class PointsOut(PointsBase):
    class Config:
        orm_mode = True
