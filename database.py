from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker




ENGINE = create_engine('postgresql://postgres:password@localhost/delivery', echo=True)

Base = declarative_base()
session = sessionmaker()

