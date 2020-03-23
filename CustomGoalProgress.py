from datetime import date
from sqlalchemy import *
from sqlalchemy.orm import relationship
from CustomGoal import CustomGoal
from ModelHandler import *

class CustomGoalProgress(Base):
    __tablename__ = 'CustomGoalProgress'

    username = Column(String, primary_key=True, nullable=False)
    goal_id = Column(ForeignKey('CustomGoal.id', ondelete='CASCADE'), primary_key=True, nullable=False)
    date = Column(Text, primary_key=True, nullable=False)
    isMet = Column(Integer, nullable=False)

    goal = relationship('CustomGoal')

    def addCustomGoalProgress(self, username, goalId, date, isMet):
        session = make_session()
        record = session.query(CustomGoalProgress)\
                        .filter(CustomGoalProgress.username == username,
                                CustomGoalProgress.goal_id == goalId)\
                        .all()
        # if record is None:
        customGoalProgress = CustomGoalProgress()
        customGoalProgress.username = username
        customGoalProgress.goal_id = goalId
        customGoalProgress.isMet = isMet
        customGoalProgress.date = date
        session.add(customGoalProgress)
        # else:
        #     record.isMet = isMet
        session.commit()  # need to commit for changes to appear in database
        session.close()


    def deleteCustomGoal(self, username, goalId):
        session = sessionmaker(bind=engine)
        session = session()
        session.delete(username, goalId)
        session.commit() # need to commit for changes to appear in database

        session.close()


if __name__ == '__main__':
    c = CustomGoalProgress()
    c.addCustomGoalProgress('Munbodh21', 1, date.today(), False)