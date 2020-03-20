import User
from datetime import datetime,date
from sqlalchemy import *
from sqlalchemy.dialects.sqlite import DATE
from sqlalchemy.ext.declarative import *
from sqlalchemy.orm import sessionmaker, relationship
from ModelHandler import *

class UserMeal(Base):
    __tablename__ = 'UserMeal'

    consumptionId = Column(Integer, primary_key=True)
    foodId = Column(ForeignKey('FoodDictionary.foodId'))
    username = Column(ForeignKey('User.username'), nullable=False)
    caloriesEatenPerFood = Column(Float, nullable=False)
    dateIntake = Column(Text, server_default=text("NULL"))

    FoodDictionary = relationship('FoodDictionary')
    User = relationship('User')

    def totalCalorieToday(self, username):
        #fetch username
        #for that username, fetch for today's date, all the calories
        #add up the calories here
        session = make_session()
        calEaten = session.query(func.sum(UserMeal.caloriesEatenPerFood).label('caloriesConsumed'))\
                          .filter(UserMeal.dateIntake == datetime.today().strftime('%d/%m/%Y'),
                                  UserMeal.username == username)\
                          .group_by(UserMeal.username).first()
        session.close()
        return calEaten[0] if calEaten is not None else 0


def main():
    pass
    # Base.metadata.create_all(bind=engine)
    # Session = sessionmaker(bind=engine)
    # session = Session()


if __name__ == '__main__':
    main()