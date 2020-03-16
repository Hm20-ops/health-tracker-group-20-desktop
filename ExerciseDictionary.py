from sqlalchemy import Column, String, REAL, INTEGER

from ModelHandler import Base, make_session, engine


class ExerciseDictionary(Base):
    __tablename__ = "ExerciseDictionary"
    exerciseId=Column(INTEGER,primary_key=True,autoincrement=True)
    activity = Column(String, primary_key=False)  # these attributes map directly to columns in the table
    specificMotion = Column(String, unique=False)
    metValue = Column(REAL)
    @staticmethod
    def addExercise(activity,specificMotion,metValue):
        session=make_session()
        addExercise=ExerciseDictionary(activity=activity,specificMotion=specificMotion,metValue=metValue)
        session.add(addExercise)
        session.commit()
        session.close()







def main():
    Base.metadata.create_all(engine)





if __name__ == "__main__":
    main()






