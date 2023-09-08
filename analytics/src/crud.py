from sqlalchemy.orm import Session, load_only
from common.models import Daily


def get_etf(db: Session, fund_symbol: str):
    return db.query(Daily).filter(Daily.fund_symbol == fund_symbol).all()


def get_all_etf_symbols(db: Session):
    results = db.query(Daily).options(load_only(Daily.fund_symbol)).all()
    return {i.fund_symbol for i in results}


def get_etf_statistics(db: Session, fund_symbol: str, requested_date: str):
    return (
        db.query(Daily)
        .filter(
            Daily.fund_symbol == fund_symbol,
            Daily.date.like(requested_date),
        )
        .one()
    )
