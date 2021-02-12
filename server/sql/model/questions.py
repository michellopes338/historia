from sqlalchemy import Column, String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import relationship

from ..connection import Base


class Questions(Base):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True)
    question = Column(String)
    alternatives_fk = relationship('Alternatives')


class Alternatives(Base):
    __tablename__ = 'alternatives'

    id = Column(Integer, primary_key=True)
    alternative = Column(String)
    is_correct = Column(Boolean, default=False)
    questions_fk = Column(Integer, ForeignKey('questions.id'))
