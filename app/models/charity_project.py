from sqlalchemy import Column, String, Text

from app.core.db import Base, DonationMixin


class CharityProject(DonationMixin, Base):

    name = Column(String(100))
    description = Column(Text)
