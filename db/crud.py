# get usr, add user, delete user, get todo, add todo, update todo, delete todo
from .models import user_table, todo_table
from sqlalchemy.orm import Session
from fastapi.exceptions import HTTPException
from fastapi import status


# get user by email
async def get_user_by_email(email: str, db: Session):
    return await db.query(user_table).filter(user_table.email == email).first()


# create new user
async def create_user(usr_email: str, usr_password: str, db: Session):
    db_user = db.query(user_table).filter(user_table.email == usr_email).first()
    if not db_user:
        new_user = user_table(email=usr_email, password=usr_password)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return {"message": "user created", "id": new_user.id}
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, detail="user email already exists"
    )


# delete user
async def delete_user_by_email(usr_email: str, db: Session):
    db_user = await db.query(user_table).filter(usr_email).first()
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="user email does not exist"
        )
    db.delete(db_user)
    db.commit()
    db.refresh(db_user)


# get todo by id
async def get_todo_by_id(usr_id: int, db: Session) -> any:
    db_todo = await db.query(todo_table).filter(usr_id).first()
    if not db_todo:
        HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="todo does not exist"
        )
    return db_todo


# get all todos
async def get_all_todo(email: str, db: Session) -> any:
    db_todo = await db.query(todo_table).filter(email).all()
    if not db_todo:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="empty todo"
        )
    return db_todo


# create todo
async def create_todo(usr_task: str, usr_id: int, db: Session):
    db_user = db.query(user_table).filter(usr_id).first()
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="invalid user id"
        )
    new_todo = todo_table(task=usr_task, user_id=usr_id)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)


# update todo
async def update_todo(todo_id: int, new_task: str, db: Session):
    db_todo = db.query(todo_table).filter(todo_id).first()
    if not db_todo:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="todo id does not exist"
        )
    update_td = todo_table(task=new_task)
    db.add(update_td)
    db.commit()
    db.refresh()


# delete todo
async def delete_todo(todo_id: int, db: Session) -> bool:
    db_todo = await db.query(todo_table).filter(todo_id).first()
    if not todo_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="invalid todo id"
        )
    db.delete(db_todo)
    db.commit()
    db.refresh(db_todo)
    return True
