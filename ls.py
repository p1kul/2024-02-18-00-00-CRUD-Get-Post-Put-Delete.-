from fastapi import FastAPI,Path

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get("/users")
async def all_inf() -> dict:
    return users

@app.post("/user/{username}/{age}")
async def create_message(username: str = Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")
                         , age: str = Path(ge=18, le=120, description="Enter age",example="24")) -> str:
    user_id = str(int(max(users,key=int)) + 1)
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is registered"

@app.put("/user/{user_id}/{username}/{age}")
async def refresh(user_id: str = Path(ge=1, le=100, description="Enter User ID", example="1")
                  , username: str = Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")
                  , age: str = Path(ge=18, le=120, description="Enter age",example="24")) -> str:
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} is registered"

@app.delete("/user/{user_id}")
async def delete(user_id: str = Path(ge=1, le=100, description="Enter User ID", example="1")) -> str:
    users.pop(user_id)








