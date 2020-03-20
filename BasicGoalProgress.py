from sqlalchemy import ForeignKey, Text, Float
from sqlalchemy.orm import relationship
from sqlalchemy.testing.schema import Column

from ModelHandler import *

class BasicGoalProgress(Base):
    __tablename__ = 'BasicGoalProgress'

    username = Column(ForeignKey('User.username', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False)
    date = Column(Text, primary_key=True, nullable=False)
    weight = Column(Float, nullable=False)

    User = relationship('User')
