from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from common.models import Daily
from common.database import SessionLocal
from src.crud import get_etf, get_all_etf_symbols, get_etf_statistics

from typing import List

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/etf/{etf_id}/volume")
async def get_max_daily_volume(etf_id: str, db: Session = Depends(get_db)):
    daily_results: List[Daily] = get_etf(db, etf_id)
    volumes = [i.volume for i in daily_results]
    return {"max_volume": max(volumes)}


@router.get("/etf")
async def get_etf_id(db: Session = Depends(get_db)):
    etf_symbols = get_all_etf_symbols(db)
    return {"etf_symbols": etf_symbols}


@router.get("/etf/{etf_id}/{requested_date}")
async def get_etf_daily_stats(
    etf_id: str, requested_date: str, db: Session = Depends(get_db)
):
    daily_results: List[Daily] = get_etf_statistics(db, etf_id, requested_date)
    return {"daily_results": daily_results.to_json()}
