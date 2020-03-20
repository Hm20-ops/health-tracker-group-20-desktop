'''
TODO
1.Clean up the code
2.Add goal to Group table- must discuss first
3.Other considerations?
'''

from datetime import datetime

from alembic.operations import Operations
from alembic.runtime.migration import MigrationContext
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import relationship
from sqlalchemy import *

from alembic import op
from sqlalchemy import Column

import User
from CustomGoal import CustomGoal
from ModelHandler import *


class Group(Base):
    __tablename__ = "Group"
    groupName = Column(String, nullable=False)
    groupId = Column(Integer, primary_key=True)
    groupType = Column(Enum('OPEN', 'Restricted'), nullable=False)
    completeGoalDate = Column(Date, nullable=False)

    # Group = relationship('Group', secondary='UserInGroups')#this seemed to cause crash
    @staticmethod
    def createGroup(groupId, groupName, groupType, completeGoalDate):
        session = make_session()
        group = Group()
        group.groupName = groupName
        group.groupId = groupId
        group.groupType = groupType
        group.completeGoalDate = completeGoalDate
        session.add(group)
        session.commit()  # need to commit for changes to appear in database
        session.close()

    @staticmethod
    def get_all_group():
        session = make_session()
        # query FoodDictionary to fetch all rows
        data = session.query(Group).join(CustomGoal) \
            .with_entities(Group.groupName, CustomGoal.goal_description).all()
        session.close()
        return data

    # def __init__(self, name, type, admin=[], members=[], common_goal=None):
    #     self.__id = id(self)
    #     self.__name = name
    #     GroupType = Enum('GroupType', 'OPEN RESTRICTED')
    #     self.__type = GroupType[type.upper()]
    #     self.__admin = admin
    #     self.__members = members
    #     self.__common_goal = common_goal
    #
    # def set_goal(self, goal):
    #     self.__common_goal = goal
    #
    # def invite(self, user):
    #     self.__members.append(user)
    #
    # def goal_archived(self):
    #     return self.__common_goal.date == datetime.now()
    #
    # def send_details(self, goal):
    #     pass
    #
    # def send_goal(self, goal):
    #     pass
    #
    # def accept_user(self, user):
    #     pass
    #
    # def is_admin(self, user):
    #     return self.__admin.contains(user)
    #
    # def kick_user(self, user):
    #     if user not in self.__members:
    #         raise ValueError('User not in the group')
    #     self.__members.remove(user)


def main():
    metadata = MetaData()
    # metadata.reflect(engine)
    # Table('UserGroup', metadata,
    #       Column('username', ForeignKey('User.username'), primary_key=True),
    #       Column('groupId', ForeignKey('Group.groupId'), primary_key=True),
    #       Column('isAdmin',Boolean,nullable=False),
    #       )
    # Base = automap_base(metadata=metadata)
    # Base.prepare()
    # metadata.reflect(engine)#this is just displaying the metadata
    # metadata.create_all(engine,checkfirst=True)#checks if all other tables are instantiated
    # metadata.bind=engine
    # Table("UserGroup", metadata,
    #       Column('isAdmin', Boolean,nullable=False),
    #       extend_existing=True,#this means we can edit(i.e add) new columns without deleting table
    #       autoload=True,#works with extend_existing
    #       autoload_with=engine
    #       )
    date_str = '20-09-2018'
    date_object = datetime.strptime(date_str, '%d-%m-%Y').date()

    Group.createGroup(2, 'FatBurner', 'OPEN', date_object)



if __name__ == '__main__':
    main()
