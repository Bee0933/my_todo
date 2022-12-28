from .database import engine, Base
import logging

# create database
# pylint: disable=broad-except
def initialize_db():
    try:
        Base.metadata.create_all(bind=engine)
    except Exception as e:
        logging.exception("db create error : %s", e)
