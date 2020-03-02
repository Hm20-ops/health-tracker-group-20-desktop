from sqlalchemy.orm import relationship
from sqlalchemy import *
from GoalInterface import GoalInterface

from ModelHandler import *


class GroupCustomGoal(Base):
    __tablename__ = 'GroupCustomGoal'
    __table_args__ = (
        CheckConstraint('act_frequency > 0'),
        CheckConstraint('act_period_length > 0'),
        CheckConstraint('checkin_interval >= 0'),
        CheckConstraint('isMet in (0,1)'),
        CheckConstraint('pass_interval <= checkin_interval')
    )

    id = Column(Integer, primary_key=True)
    groupId = Column(ForeignKey('Group.groupId', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    goal_description = Column(Text, nullable=False)
    date = Column(Date, nullable=False)
    isMet = Column(Integer, nullable=False)
    checkin_interval = Column(Integer, nullable=False)
    act_frequency = Column(Integer, nullable=False)
    act_period_length = Column(Integer, nullable=False)
    pass_interval = Column(Integer, nullable=False)

    Group = relationship('Group')

    def set_date(self, date):
        self.date = date

    def get_report(self):
        super()

    def set_checkin_duration(self, days):
        super()

    def get_progress(self):
        self.get_report();


class UserCustomGoal(Base):
    __tablename__ = 'UserCustomGoal'
    __table_args__ = (
        CheckConstraint('act_frequency > 0'),
        CheckConstraint('act_period_length > 0'),
        CheckConstraint('checkin_interval >= 0'),
        CheckConstraint('isGroupGoal in (0,1)'),
        CheckConstraint('isMet in (0,1)'),
        CheckConstraint('pass_interval <= checkin_interval')
    )

    id = Column(Integer, primary_key=True)
    username = Column(ForeignKey('User.username', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    goal_description = Column(Text, nullable=False)
    date = Column(Date, nullable=False)
    isMet = Column(Integer, nullable=False)
    isGroupGoal = Column(Integer, nullable=False)
    checkin_interval = Column(Integer, nullable=False)
    act_frequency = Column(Integer, nullable=False)
    act_period_length = Column(Integer, nullable=False)
    pass_interval = Column(Integer, nullable=False)

    User = relationship('User')

    def set_date(self, date):
        self.date = date

    def get_report(self):
        super()

    def set_checkin_duration(self, days):
        super()

    def get_progress(self):
        self.get_report();


def main():
    print()


if __name__ == '__main__':
    main()