from datetime import datetime

from app.core.db import Base
from sqlalchemy import Boolean, Column, DateTime, Integer


class DonationMixin(Base):
    """Родительский класс для моделей CharityProject и Donation."""
    __abstract__ = True

    full_amount = Column(Integer)
    invested_amount = Column(Integer, default=0)
    fully_invested = Column(Boolean, default=False)
    create_date = Column(DateTime, default=datetime.now)
    close_date = Column(DateTime)
