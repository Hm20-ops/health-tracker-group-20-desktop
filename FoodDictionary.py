from sqlalchemy import Column, String, REAL, INTEGER

from ModelHandler import Base, make_session


class FoodDictionary(Base):
    __tablename__ = "FoodDictionary"
    foodId=Column(INTEGER, primary_key=True,autoincrement=True)
    foodName = Column(String, primary_key=False)  # these attributes map directly to columns in the table
    calories = Column(REAL, unique=False)

    @staticmethod
    def addFood(foodName, calories):
        session = make_session()
        print(foodName)
        print(calories)
        addFood = FoodDictionary(foodName=foodName, calories=float(calories))
        session.add(addFood)
        session.commit()
        session.close()

    @staticmethod
    def get_all_food():
        session = make_session()
        # query FoodDictionary to fetch all rows
        data = session.query(FoodDictionary) \
            .with_entities(FoodDictionary.foodName, FoodDictionary.calories).all()
        session.close()
        return data

    def get(self, index):
        session = make_session()
        food = session.query(FoodDictionary).get(index)  # for an index in table, query correspoding baseCalorie
        session.close()
        return food

    def getFoodId(self, foodName):
        session = make_session()
        food = session.query(FoodDictionary)
        return food


if __name__ == "__main__":
    # Base.metadata.create_all(engine)
    fd = FoodDictionary()
    food = fd.getFoodId('Alfalfa sprouts, raw')
    print(food)
