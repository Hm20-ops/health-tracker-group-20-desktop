from sqlalchemy import String, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.testing.schema import Column

from ModelHandler import *

class CustomGoalProgres(Base):
    __tablename__ = 'CustomGoalProgress'

    username = Column(String, primary_key=True, nullable=False)
    goal_id = Column(ForeignKey('CustomGoal.id', ondelete='CASCADE'), primary_key=True, nullable=False)
    date = Column(Text, primary_key=True, nullable=False)
    isMet = Column(ForeignKey('CustomGoal.id'), nullable=False)

    goal = relationship('CustomGoal', primaryjoin='CustomGoalProgres.goal_id == CustomGoal.id')
    CustomGoal = relationship('CustomGoal', primaryjoin='CustomGoalProgres.isMet == CustomGoal.id')
