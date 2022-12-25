# pylint: disable=fixme
from .database import Base
from sqlalchemy import Column, String, Integer, Text, ForeignKey, DateTime
import datetime


# user table
class user_table(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String(), unique=True, nullable=False)
    password = Column(String(), nullable=False)

    def __repr__(self) -> str:
        return f" id : {self.id}"


# todo table
class todo_table(Base):
    __tablename__ = "todo"
    id = Column(Integer, primary_key=True)
    task = Column(Text(), nullable=False)
    time_posted = Column(DateTime, default=datetime.datetime.now(datetime.timezone.utc))
    user_id = Column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )

    def __repr__(self) -> str:
        return f" id : {self.id}"
