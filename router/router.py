from fastapi import APIRouter
from schema.user_schema import UserSchema 
from config.database import conn
from model.user import users
from werkzeug.security import generate_password_hash, check_password_hash

user = APIRouter()

@user.get("/")
def root():
    return {"message": "Hi, I'm FastAPI with a router."}

@user.post("/api/user")
def create_user(data_user: UserSchema):
    new_user = data_user.dict()
    new_user["kpasswd"] = generate_password_hash(data_user.kpasswd, "pbkdf2:sha256:30", 30)
    conn.execute(users.insert().values(new_user))
    conn.commit()
    conn.close()
    return "Success"

@user.put("/api/user")
def update_user():
    pass