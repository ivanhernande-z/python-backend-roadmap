from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import HTTPException


class user(BaseModel):
    name : str
    email : str
    age : int

users = []


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/users")
def create_user(user: user):
    user_dict = user.dict()
    user_dict["id"] = len(users) + 1
    users.append(user_dict)
    return user_dict


@app.get("/users")
def get_users():
    return users

@app.get("/users/{user_id}")
def get_user(user_id : int) :
    for user in users:
        if user["id"] == user_id:
            return user
        raise HTTPException(status_code=404, detail="Item not found papi")
    

@app.delete("/users/{user_id}")
def delete_user(user_id : int) :
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            return {"message:" : "user deleted papi"}
        raise HTTPException(status_code=404, detail="Item not found papi")