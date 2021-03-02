from fastapi import APIRouter, Path, Depends, Body
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from ..sql import crud, model, schemas
from ..sql.connection import get_db


router = APIRouter()

@router.get('/ranking/{pts}')
def get_position(db: Session = Depends(get_db), pts: int = Path(...)):
    return crud.ranking.get_position(db, pts)


@router.post('/ranking')
def insert_points(db: Session = Depends(get_db), points: int = Body(...)):
    return crud.ranking.insert_points(db, points)
