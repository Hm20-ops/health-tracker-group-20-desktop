import User
from datetime import datetime,date
from sqlalchemy import *
from sqlalchemy.dialects.sqlite import DATE
from sqlalchemy.ext.declarative import *
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()
engine = create_engine('sqlite:///User.db', echo=True)

class Drink(Base):
    __tablename__ = 'Drink'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)


class Food(Base):
    __tablename__ = 'Food'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)


class UserMeal(Base):
    __tablename__ = 'UserMeal'

    username = Column(ForeignKey('User.username', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False)
    meal_id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)

    # foreign keys definition to user table
    User = relationship('User')


class DrinkConsumed(Base):
    __tablename__ = 'DrinkConsumed'
    __table_args__ = (
        CheckConstraint('quantity>0'),
    )

    username = Column(ForeignKey('UserMeal.username', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False)
    meal_id = Column(ForeignKey('UserMeal.meal_id', ondelete='CASCADE'), primary_key=True, nullable=False)
    drink_id = Column(ForeignKey('Drink.id', ondelete='RESTRICT'), nullable=False)
    quantity = Column(Integer, nullable=False)

    # foreign keys definitions
    drink = relationship('Drink')
    meal = relationship('UserMeal', primaryjoin='DrinkConsumed.meal_id == UserMeal.meal_id')
    UserMeal = relationship('UserMeal', primaryjoin='DrinkConsumed.username == UserMeal.username')


class FoodConsumed(Base):
    __tablename__ = 'FoodConsumed'
    __table_args__ = (
        CheckConstraint('quantity>0'),
    )

    username = Column(ForeignKey('UserMeal.username', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False)
    meal_id = Column(ForeignKey('UserMeal.meal_id', ondelete='CASCADE'), primary_key=True, nullable=False)
    food_id = Column(ForeignKey('Food.id', ondelete='RESTRICT'), nullable=False)
    quantity = Column(Integer, nullable=False)

    # foreign keys definitions
    food = relationship('Food')
    meal = relationship('UserMeal', primaryjoin='FoodConsumed.meal_id == UserMeal.meal_id')
    UserMeal = relationship('UserMeal', primaryjoin='FoodConsumed.username == UserMeal.username')


def main():
    Base.metadata.create_all(bind=engine)
    # Session = sessionmaker(bind=engine)
    # session = Session()


if __name__ == '__main__':
    main()