from endpoints import auth_router
from fastapi import FastAPI
import uvicorn

app = FastAPI()

app.include_router(auth_router)


if __name__ == "__main__":
    uvicorn.run(app=app, host="0.0.0.0", port=8001)
