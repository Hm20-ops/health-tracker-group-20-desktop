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

    def get_all_exercises(self):
        session = make_session()
        data = session.query(ExerciseDictionary)\
                      .with_entities(ExerciseDictionary.specificMotion, ExerciseDictionary.metValue).all()

        session.close()
        return data

    def get(self, index):
        session = make_session()
        food = session.query(ExerciseDictionary).get(index)  # for an index in table, query correspoding baseCalorie
        session.close()
        return food





def main():
    Base.metadata.create_all(engine)





if __name__ == "__main__":
    main()






