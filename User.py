# To do:
# 1.Optimise imports
# 2.Reformat dob into dd/mm/yyyy
# 3.Think about how to store group arrays
# 4.Define all database constraints

import enum
import re
from datetime import datetime

from sqlalchemy import *
from sqlalchemy import types, create_engine
from sqlalchemy.dialects.sqlite import DATE
from sqlalchemy.ext.declarative import *
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///User.db', echo=True)


class Gender(enum.Enum):
    male = 1
    female = 2
    other = 3


class User(Base):
    __tablename__ = "User"
    # We do not need to define a constructor. See main() for example
    username = Column('username', String, primary_key=True)  # these attributes map directly to columns in the table
    email = Column('email', String, unique=True)
    password = Column('password', String)
    name = Column('name', String)
    dob = Column('dob', DATE(
        storage_format="%(month)02d/%(day)02d/%(year)04d",
        regexp=re.compile("(?P<month>\d+)/(?P<day>\d+)/(?P<year>\d+)")
    ))  # impose strict formatting mm-dd-yyyy
    age = Column('age', INTEGER)
    weight = Column('weight', INTEGER)
    height = Column('height', REAL)
    gender = Column(types.Enum('male', 'female', 'other'), nullable=false)

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
    session = Session()
    user = User()
    user.dob = "12/20/1999"
    user.password = "peen"
    user.username = "micro peen"
    user.email = "@gmail.com"
    user.name = "peenocchio"
    user.gender = 'male'
    date_str = '09-19-2018'
    date_object = datetime.strptime(date_str, '%m-%d-%Y').date()
    user.dob=date_object

    session.add(user)
    session.commit()
    session.close()


if __name__ == '__main__':
    main()
