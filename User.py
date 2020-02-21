'''
TODO:
    1.Optimise imports
    2.Define all database constraints
'''
from enum import Enum
import re
import Group
from datetime import datetime,date

from sqlalchemy import *
from sqlalchemy import types, create_engine
from sqlalchemy.dialects.sqlite import DATE
from sqlalchemy.ext.declarative import *
from sqlalchemy.orm import sessionmaker



Base = declarative_base()
engine = create_engine('sqlite:///User.db', echo=True)


# class Gender(Enum):
#     male = 1
#     female = 2
#     other = 3


class User(Base):
    __tablename__ = "User"
    # We do not need to define a constructor. See main() for example
    username = Column(String, primary_key=True)  # these attributes map directly to columns in the table
    email = Column(String, unique=True)
    password = Column(String)
    name = Column(String)
    dob = Column(DATE(
        storage_format="%(day)02d/%(month)02d/%(year)04d",
        regexp=re.compile("(?P<day>\d+)/(?P<month>\d+)/(?P<year>\d+)")
    ))  # impose strict formatting dd-mm-yyyy
    age = Column(INTEGER)
    weight = Column(REAL)         #both weight and height should be real
    height = Column(REAL)
    gender = Column(Enum('male', 'female', 'other'), nullable=false)

    def create_group(self):
        # Create a new group
        group_goal = None
        group = Group('name', 'OPEN', [self], [self], group_goal)
        self.__groups.append(group)

    def join_group(self, id):
        pass

    def leave_group(self):
        pass

    def edit_details(self):
        pass

    def create_goal(self):
        pass

    def create_exercise(self):
        pass

    def create_diet(self):
        pass

    def age_calculator(self):
        today = date.today()
        age = today.year - self.dob.year -((today.month, today.day) <(self.dob.month, self.dob.day))
        return age

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
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()#we interact with db file in a session

    user = User()
    user.password = "Hemal20"
    user.username = "Munbodh20"
    user.email = "munbodhhemal20@gmail.com"
    user.name = "Hemal Munbodh"
    user.gender = 'male'
    date_str = '20-05-1999'
    date_object = datetime.strptime(date_str, '%d-%m-%Y').date()#converting a date string to date object. See format
    user.dob=date_object
    user.age=user.age_calculator()#mitigates error of inputting wrong age


    session.add(user)
    session.commit()#need to commit for changes to appear in database

    session.close()


if __name__ == '__main__':
    main()
