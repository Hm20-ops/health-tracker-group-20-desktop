from sqlalchemy.orm import relationship
from sqlalchemy import *
from GoalInterface import GoalInterface
from ModelHandler import *
from User import User

class BasicGoal(User):
    __tablename__ = 'BasicGoal'
    __table_args__ = (
        CheckConstraint('isMet in (0 ,1)'),
    )

    username = Column(ForeignKey('User.username', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True)
    target_weight = Column(Float, nullable=False)
    date = Column(Date, nullable=False)
    isMet = Column(Integer, nullable=False)


    def set_date(self, date):
        self.date = date

    def get_report(self):
        super()

    def set_checkin_duration(self, days):
        super()

    def get_progress(self):
        self.get_report()

    def is_target_met(self):
        return self.meet


def main():
    print()


if __name__ == '__main__':
    main()