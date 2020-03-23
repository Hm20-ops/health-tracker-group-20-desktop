import re
#import Group
from datetime import datetime,date

from sqlalchemy import *
from sqlalchemy.dialects.sqlite import DATE
from sqlalchemy.orm import relationship, query

from ModelHandler import *

class UserGroup(Base):
    tablename = 'UserGroup'

    username = Column(ForeignKey('User.username'), primary_key=True, nullable=False)
    groupId = Column(ForeignKey('Group.groupId'), primary_key=True, nullable=False)
    isAdmin = Column(Boolean, nullable=False)

    Group = relationship('Group')
    User = relationship('User')

    def createUserGroup(self, username, groupId):
        session = make_session()
        userGroup = UserGroup()
        userGroup.username = username
        userGroup.groupId = groupId
        userGroup.isAdmin = True
        session.add(userGroup)
        session.commit()  # need to commit for changes to appear in database
        session.close()

    def addUserGroup(self, username, groupId):
        session = make_session()
        userGroup = UserGroup()
        userGroup.username = username
        userGroup.groupId = groupId
        userGroup.isAdmin = False
        session.add(userGroup)
        session.commit()  # need to commit for changes to appear in database
        session.close()

    def setAdmin(self, username, groupId):
        session = make_session()
        record = session.query(UserGroup)\
                        .filter(UserGroup.username == username,
                                UserGroup.groupId == groupId)\
                        .first()
        record.isAdmin = True
        session.close()

    def isAdmin(self, username, groupId):
        session = make_session()
        record = session.query(UserGroup)\
                        .filter(UserGroup.username == username,
                                UserGroup.groupId == groupId)\
                        .first()
        session.close()
        return record.isAdmin

    def leaveGroup(self, username, groupId):
        session = make_session()
        record = session.query(UserGroup)\
                        .filter(UserGroup.username == username,
                                UserGroup.groupId == groupId)\
                        .first()
        session.delete(record)
        session.commit()  # need to commit for changes to appear in database
        session.close()

