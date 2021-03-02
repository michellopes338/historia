# from typing import ...
from sqlalchemy.orm import Session

from .. import model, schemas
from .crud_base import CRUD


class PointsCRUD(CRUD[model.Ranking, schemas.PointsIn, schemas.PointsUpdate]):
    def get_position(self, database: Session, pts: int):
        length_db = database.query(self.model).count()
        position = database.query(self.model).filter(self.model.points >= pts).count()

        return 100 - position * 100 / length_db
    
    def insert_points(self, database: Session, points: int):
        points_db = model.Ranking(
            points=points
        )

        database.add(points_db)
        database.commit()
        database.refresh(points_db)

        return points_db

    
ranking = PointsCRUD(model.Ranking)
