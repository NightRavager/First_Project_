from sqlalchemy.orm import Session
from src.main.api.db.models.credit_table import Credit


class CreditCrudDb:
    @staticmethod
    def get_credit_by_credit_id(db: Session, account_id: int) -> type[Credit] | None:
        return db.query(Credit).filter_by(id=account_id).first()

    @staticmethod
    def delete_credit(db: Session, account_id: int) -> None:
        credit = db.query(Credit).filter_by(id=account_id).first()
        if credit:
            db.delete(credit)
            db.commit()
