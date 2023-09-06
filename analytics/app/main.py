from fastapi import FastAPI

from .routers import courses, etf

app = FastAPI()

app.include_router(etf.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}
