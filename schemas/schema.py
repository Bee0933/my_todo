# signin, login, create todo, modify todo
# pylint: disable=no-name-in-module
from pydantic import BaseModel, Field, EmailStr
from fastapi_utils.enums import StrEnum
from enum import auto


# sort schema
class sortOption(StrEnum):
    asc = auto()
    desc = auto()
    none = auto()


class usr_account_schema(BaseModel):
    email: EmailStr = Field(default=None, description="user email for signin/signup")
    password: str = Field(
        default=None, min_length=8, description="user password for security"
    )


class usr_todo_schema(BaseModel):
    task: str = Field(default=None, description="todo tasks")
    usrID: int = Field(
        default=None, max_digits=3, description="user Identification form users table"
    )
