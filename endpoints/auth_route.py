# signin, login,
from db import sessionLocal, create_user
from fastapi import APIRouter, status, Depends
from fastapi.exceptions import HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlalchemy.orm import Session
from .security import HashPassword


auth_router = APIRouter(prefix="/auth", tags=["authentication"])

security = HTTPBasic()


# dependency
def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()


# singup route
@auth_router.post("signup/", status_code=status.HTTP_201_CREATED)
async def signup(credentials: HTTPBasicCredentials, db: Session = Depends(get_db)):
    if not credentials:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="input authentication credentials",
        )
    sec = HashPassword()
    user_password = sec.create_hash(credentials.password)
    return await create_user(credentials.username, user_password, db)
