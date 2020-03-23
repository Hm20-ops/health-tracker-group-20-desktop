from sqlalchemy.orm import relationship
from sqlalchemy import *
from ModelHandler import *
from User import User

class BasicGoal(Base):
    __tablename__ = 'BasicGoal'
    __table_args__ = (
        CheckConstraint('isMet in (0 ,1)'),
    )
    User = relationship('User')
    username = Column(ForeignKey('User.username', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True)
    target_weight = Column(Float, nullable=False)
    date = Column(Date, nullable=False)
    isMet = Column(Boolean, nullable=False)


    def get(self, username):
        session = make_session()
        basic_goal = session.query(BasicGoal).filter(BasicGoal.username == username).all()
        session.close()
        return basic_goal

    def create_basic_goal(self, username,target_weight, date, isMet=False):
        session = make_session()
        basic_goal = BasicGoal()
        basic_goal.username = username
        basic_goal.target_weight = target_weight
        basic_goal.date = date
        basic_goal.isMet = isMet
        session.add(basic_goal)
        session.commit()
        session.close()

def main():
    print()


if __name__ == '__main__':
    main()