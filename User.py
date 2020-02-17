from enum import Enum
import datetime

import sqlalchemy
from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship

#from Group import Group
from GoalInterface import GoalInterface

Base = declarative_base()
engine = create_engine('sqlite:///User.db', echo=True)


class User(Base):
    __tablename__ = "User"

    username = Column('username', String, primary_key=True)
    email = Column('email', String, unique=True)
    password = Column('password', String)
    name = Column('name', String)

    #
    # def __init__(self, username, name, email, dob, password, gender, age, weight, height):
    #     #load account details
    #     self.__username = username
    #     self.__email = email
    #     self.__password = password
    #     # load user details
    #     self.__name = name
    #     self.__dob = datetime.datetime.strptime(dob, "%d/%m/%Y").date()
    #     Gender = Enum('Gender', 'Male Female')
    #     self.__gender = Gender[gender.upper()]
    #     self.__age = age
    #     self.__weight = weight
    #     self.__height = height
    #     self.__goals = []
    #     self.__groups = []
    #     print('\n'.join("%s: %s" % item for item in vars(self).items()))
    #
    # def create_group(self):
    #     """
    #
    #     """
    #     # Create a new group
    #     group_goal = None
    #     group = Group('name', 'OPEN', [self], [self], group_goal)
    #     self.__groups.append(group)
    #
    # def join_group(self, id):
    #     pass
    #
    # def leave_group(self):
    #     pass
    #
    # def edit_details(self):
    #     pass
    #
    # def create_goal(self):
    #     pass
    #
    # def create_exercise(self):
    #     pass
    #
    # def create_diet(self):
    #     pass



def main():
    #Base.metadata.create_all(bind=engine)
    Session=sessionmaker(bind=engine)
    session=Session()
    users=session.query(User).all()
    for user in users:
        print('\n'.join("%s: %s" % item for item in vars(user).items()))

if __name__ == '__main__':
    main()
