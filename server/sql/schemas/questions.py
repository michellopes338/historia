from typing import Optional, Tuple
from pydantic import BaseModel


class AlternativesBase(BaseModel):
    id: int
    alternative: str


class AlternativesUpdate(BaseModel):
    alternative: Optional[str]


class AlternativesIn(BaseModel):
    alternative: str
    is_correct: bool
    question_fk: int


class AlternativesOut(AlternativesBase):
    class Config:
        orm_mode = True


class QuestionsBase(BaseModel):
    id: int
    question: str


class QuestionsUpdate(BaseModel):
    question: Optional[str]


class QuestionsIn(BaseModel):
    question: str


class QuestionsOut(QuestionsBase):
    alternatives: Tuple[AlternativesBase]
    class Config:
        orm_mode = True
