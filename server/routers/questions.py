from fastapi import APIRouter, Path, Depends, Body
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from ..sql import crud, model, schemas
from ..sql.connection import get_db


router = APIRouter()

@router.get('/get-question/{id}')
def get_question_by_id(db: Session = Depends(get_db), id: int = Path(...)):
    return crud.questions.get_question_by_id(database=db, id=id)

@router.get('/verify/{id}/{answer}')
def verify(db: Session = Depends(get_db), answer: str = Path(...), id: int = Path(...)):
    return crud.questions.verify(db, id, answer)
