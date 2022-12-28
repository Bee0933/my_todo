from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session
from decouple import config

# create database engine
engine = create_engine(url=config("CONECTION_STR"), echo=True)

# init base class
Base = declarative_base()

# create database session instance
sessionLocal = scoped_session(sessionmaker(bind=engine))
