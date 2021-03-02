# from typing import ...
from sqlalchemy.orm import Session

from .. import model, schemas
from .crud_base import CRUD


class QuestionsCRUD(CRUD[model.Questions, schemas.QuestionsIn, schemas.QuestionsUpdate]):
    def get_question_by_id(self, database: Session, id: int) -> schemas.QuestionsOut:
        question = database.query(self.model.question).filter_by(id=id).first()[0]
        alternatives = database.query(model.Alternatives.alternative).filter_by(questions_fk=id).all()

        full_question = {
            'question': question,
            'alternatives': (alternative[0] for alternative in alternatives)
        }

        return full_question

    def verify(self, database: Session, id: int, answer: str):
        return database.query(model.Alternatives.is_correct).filter_by(alternative=answer).first()[0]


questions = QuestionsCRUD(model.Questions)
