from sqlalchemy import Column, ForeignKey, Integer, Text

from .union_base import DonationMixin


class Donation(DonationMixin):

    comment = Column(Text)
    user_id = Column(Integer, ForeignKey('user.id'))
