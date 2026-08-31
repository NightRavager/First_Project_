from sqlalchemy.orm import Session

from api.db.models.transaction_table import Transaction


class TransactionCrudDb:
    @staticmethod
    def get_transaction_by_from_account_id(db: Session, account_id: int) -> type[Transaction] | None:
        return db.query(Transaction).filter_by(from_account_id=account_id).first()

    @staticmethod
    def delete_transaction(db: Session, account_id: int) -> None:
        transaction = db.query(Transaction).filter_by(id=account_id).first()
        if transaction:
            db.delete(transaction)
            db.commit()
