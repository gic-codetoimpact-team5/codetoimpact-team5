from sqlalchemy.orm import Session, load_only

from . import models

def get_etf(db: Session, fund_symbol: str):
    return db.query(models.Daily).filter(models.Daily.fund_symbol == fund_symbol).all()

def get_all_etf_symbols(db: Session):
    results = db.query(models.Daily).options(load_only(models.Daily.fund_symbol)).all()
    return {i.fund_symbol for i in results}

def get_etf_statistics(db: Session, fund_symbol: str, requested_date: str):
    return db.query(models.Daily).filter(models.Daily.fund_symbol == fund_symbol, models.Daily.date.like(requested_date)).one()