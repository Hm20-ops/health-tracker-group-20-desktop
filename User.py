'''
TODO:
    1.Optimise imports
    2.Define all database constraints
'''
from enum import Enum
import re
#import Group
from datetime import datetime,date

from sqlalchemy import *
from sqlalchemy.dialects.sqlite import DATE

from ModelHandler import *

# Base = declarative_base()
# engine = create_engine('sqlite:///User.db', echo=True)


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
    gender = Column(Enum('male', 'female', 'other'), nullable=false)#

    def create_user(self, username, email, password, name, dob, weight, height, gender):
        # Session = sessionmaker(bind=engine)
        # session = Session()  # we interact with db file in a session
        session = make_session()
        user = User()
        user.password = password
        user.username = username
        user.email = email
        user.name = name
        user.gender = gender
        date_object = datetime.strptime(dob, '%d/%m/%Y').date()  # converting a date string to date object. See format
        user.dob = date_object
        user.age = user.age_calculator()
        user.weight = weight
        user.height = height

        session.add(user)
        session.commit()  # need to commit for changes to appear in database

        session.close()

    def create_group(self):
        # Create a new group
        group_goal = None
        group = Group('name', 'OPEN', [self], [self], group_goal)
        self.__groups.append(group)

    def join_group(self, id):
        pass

    def leave_group(self):
        pass

    def edit_details(self, username, email, password, name, dob, weight, height, gender):
        Session = sessionmaker(bind=engine)
        session = Session()  # we interact with db file in a session
        self.password = password
        self.username = username
        self.email = email
        self.name = name
        self.gender = gender
        date_object = datetime.strptime(dob, '%d-%m-%Y').date()  # converting a date string to date object. See format
        self.dob = date_object
        self.age = self.age_calculator()
        self.weight = weight
        self.height = height

        session.commit()  # need to commit for changes to appear in database
        session.close()

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

    def make_session(self):
        Session = sessionmaker(bind=engine)
        session = Session()
        return session

def main():
    #Base.metadata.create_all(bind=engine)
    # Session = sessionmaker(bind=engine)
    # session = Session()#we interact with db file in a session
    #
    user = User()
    # user.password = "Hemal20"
    # user.username = "Munbodh20"
    # user.email = "munbodhhemal20@gmail.com"
    # user.name = "Hemal Munbodh"
    # user.gender = 'male'
    # date_str = '20-05-1999'
    # date_object = datetime.strptime(date_str, '%d-%m-%Y').date()#converting a date string to date object. See format
    # user.dob=date_object
    # user.age=user.age_calculator()#mitigates error of inputting wrong age
    #
    #
    # session.add(user)
    # session.commit()#need to commit for changes to appear in database
    #
    # session.close()

    user.create_user("Munbodh21", "munbodhhemal21@gmail.com", "Hemal21", "Hemal Munbodh1", '21/05/1999', "65", "175", "male")

if __name__ == '__main__':
    main()
