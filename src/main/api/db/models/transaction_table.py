from sqlalchemy import Column, Integer, Float, String, ForeignKey, DateTime

from src.main.api.db.base import Base


class Transaction(Base):
    __tablename__="transaction"
    id = Column(Integer, primary_key=True, nullable=False)
    to_account_id = Column(Integer, ForeignKey('account.id'), unique=True, nullable=False)
    from_account_id = Column(Integer, ForeignKey('account.id'), unique=True, nullable=False)
    credit_id = Column(Integer, ForeignKey('credit.term_months'), nullable=False)
    amount = Column(Float, nullable=False)
    transaction_type = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)


def __repr__(self):
    return (f'<Transaction(id={self.id}, to_account_id={self.to_account_id}, from_account_id={self.from_account_id}, credit_id={self.credit_id}, amount={self.amount},'
            f'transaciont_type={self.transaction_type}, created_at={self.created_at})>')