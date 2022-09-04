from sqlalchemy import Column, Text, ForeignKey, Integer

from app.core.db import Base, DonationMixin


class Donation(DonationMixin, Base):

    comment = Column(Text)
    user_id = Column(Integer, ForeignKey('user.id'))
