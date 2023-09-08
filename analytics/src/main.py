# test
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent))

from fastapi import FastAPI

from .routers import etf


app = FastAPI()

app.include_router(etf.router)


@app.get("/")
async def root():
    return {"message": "Server is Healthy"}
