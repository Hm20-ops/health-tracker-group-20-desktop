from datetime import date
from User import User
from sqlalchemy import *
from sqlalchemy.orm import relationship

from ModelHandler import *

class BasicGoalProgress(Base):
    __tablename__ = 'BasicGoalProgress'
    User = relationship('User')
    username = Column(ForeignKey('User.username', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False)
    date = Column(Text, primary_key=True, nullable=False)
    weight = Column(Float, nullable=False)



    def addBasicProgress(self, username, weight, date):
        session = make_session()
        record = session.query(BasicGoalProgress)\
                        .filter(BasicGoalProgress.username == username)\
                        .all()

        # if len(record) is 0:
        basicGoalProgress = BasicGoalProgress()
        basicGoalProgress.username = username
        basicGoalProgress.weight = weight
        basicGoalProgress.date = date
        session.add(basicGoalProgress)
        # else:
        #     record.weight = weight

        session.commit()  # need to commit for changes to appear in database
        session.close()


    # def deleteBasicGoal(self, username):
    #     # session = sessionmaker(bind=engine)
    #     # session = session()
    #     session = make_session()
    #
    #     session.delete(username)
    #     session.commit()  # need to commit for changes to appear in database
    #
    #     session.close()