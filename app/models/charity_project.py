from sqlalchemy import Column, String, Text

from .union_base import DonationMixin


class CharityProject(DonationMixin):

    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text)
