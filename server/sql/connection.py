from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = 'sqlite:///server/sqlite/db.sqlite'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    encoding='utf8'
)

Sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = Sessionlocal()

    try:
        yield db
    
    finally:
        db.close()
