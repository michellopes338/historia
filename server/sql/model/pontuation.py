from sqlalchemy import Column, Integer

from ..connection import Base


class Ranking(Base):
    __tablename__ = 'ranking'

    id = Column(Integer, primary_key=True)
    points = Column(Integer)