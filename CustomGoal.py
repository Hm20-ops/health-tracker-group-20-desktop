from sqlalchemy.orm import relationship
from sqlalchemy import *
from GoalInterface import GoalInterface
from sqlalchemy.sql import func
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

    def get(self, group_id):
        session = make_session()
        group_custom_goal = session.query(GroupCustomGoal).get(GroupCustomGoal.groupId == group_id).all()
        session.close()
        return group_custom_goal

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

    def get(self, username):
        session = make_session()
        user_custom_goal = session.query(UserCustomGoal).filter(UserCustomGoal.username == username).all()
        session.close()
        return user_custom_goal

    def create_custom_goal(self, username, description, date, isGroupGoal=False,
                           checkin_interval=1, act_frequency=1, act_period_length=1, pass_interval=1):
        session = make_session()
        custom_goal = UserCustomGoal()
        custom_goal.username = username
        custom_goal.description = description
        custom_goal.date = date
        custom_goal.isGroupGoal = isGroupGoal
        custom_goal.checkin_interval = checkin_interval
        custom_goal.act_frequency = act_frequency
        custom_goal.act_period_length = act_period_length
        custom_goal.pass_interval = pass_interval

        session.commit()
        session.close()

    def set_date(self, date):
        self.date = date

    def get_(self):
        super()

    def set_checkin_duration(self, days):
        super()

    def get_progress(self):
        self.get_report();

    def get_recent(self, username):
        session = make_session()
        recents = session.query(UserCustomGoal)\
                         .filter(UserCustomGoal.username == username, UserCustomGoal.isMet == 0)\
                         .order_by(UserCustomGoal.date)\
                         .limit(3).all()

        session.close()
        return recents

def main():
    print()


if __name__ == '__main__':
    main()