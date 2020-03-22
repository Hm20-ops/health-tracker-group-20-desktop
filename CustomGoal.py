from sqlalchemy.orm import relationship
from sqlalchemy import *
from GoalInterface import GoalInterface
from sqlalchemy.sql import func
from ModelHandler import *

class CustomGoal(Base):
    __tablename__ = 'CustomGoal'
    __table_args__ = (
        CheckConstraint('act_frequency>0'),
        CheckConstraint('act_period_length>0'),
        CheckConstraint('checkin_interval>=0'),
        CheckConstraint('isMet in (0,1)'),
        CheckConstraint('pass_interval<=checkin_interval')
    )

    id = Column(Integer, primary_key=True)
    username = Column(ForeignKey('User.username', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    goal_description = Column(Text, nullable=False)
    date = Column(Date, nullable=False)
    isMet = Column(Integer, nullable=False)
    checkin_interval = Column(Integer, nullable=False)
    act_frequency = Column(Integer, nullable=False)
    act_period_length = Column(Integer, nullable=False)
    pass_interval = Column(Integer, nullable=False)
    group_id = Column(ForeignKey('Group.groupId', ondelete='CASCADE'), nullable=False)

    group = relationship('Group')
    User = relationship('User')

    def get(self, username):
        session = make_session()
        user_custom_goal = session.query(CustomGoal).filter(CustomGoal.username == username).all()
        session.close()
        return user_custom_goal

    def create_custom_goal(self, username, description, date,
                           checkin_interval=1, act_frequency=1, act_period_length=1, pass_interval=1, group_id=None):
        session = make_session()
        custom_goal = CustomGoal()
        custom_goal.username = username
        custom_goal.goal_description = description
        custom_goal.date = date
        custom_goal.isMet = 0
        custom_goal.checkin_interval = checkin_interval
        custom_goal.act_frequency = act_frequency
        custom_goal.act_period_length = act_period_length
        custom_goal.pass_interval = pass_interval
        custom_goal.group_id = group_id

        session.add(custom_goal)
        session.commit()
        session.close()

    def get_recent(self, username):
        session = make_session()
        recents = session.query(CustomGoal)\
                         .filter(CustomGoal.username == username, CustomGoal.isMet == 0)\
                         .order_by(CustomGoal.date)\
                         .limit(3).all()

        session.close()
        return recents

    def goal_archived(self, id):
        session = make_session()
        user_custom_goal = session.query(CustomGoal).get(id)
        user_custom_goal.isMet = 1
        session.commit()
        session.close()


def main():
    print()


if __name__ == '__main__':
    main()