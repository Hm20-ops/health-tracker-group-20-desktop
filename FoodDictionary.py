from sqlalchemy import Column, String, REAL, INTEGER

from ModelHandler import Base, make_session, engine


class FoodDictionary(Base):
    __tablename__ = "FoodDictionary"
    foodId=Column(INTEGER, primary_key=True,autoincrement=True)
    foodName = Column(String, primary_key=False)  # these attributes map directly to columns in the table
    calories = Column(REAL, unique=False)
    @staticmethod
    def addFood(foodName, calories):
        session=make_session()
        print(foodName)
        print(calories)
        addFood = FoodDictionary(foodName=foodName, calories=float(calories))
        session.add(addFood)
        session.commit()
        session.close()
if __name__=="__main__":
    Base.metadata.create_all(engine)

