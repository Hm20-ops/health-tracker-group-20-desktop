import re
from Group import Group
from datetime import datetime,date

from sqlalchemy import *
from sqlalchemy.dialects.sqlite import DATE
from sqlalchemy.orm import relationship

from ModelHandler import *

class UserGroup(Base):
    __tablename__ = 'UserGroup'
    Group = relationship('Group')
    User = relationship('User')
    username = Column(ForeignKey('User.username'), primary_key=True, nullable=False)
    groupId = Column(ForeignKey('Group.groupId'), primary_key=True, nullable=False)
    isAdmin = Column(Integer, nullable=False, server_default=text("0"))  # to be implemented in stage 2

    def createUserGroup(self, username, groupId):
        session = make_session()
        userGroup = UserGroup()
        userGroup.username = username
        userGroup.groupId = groupId
        session.add(userGroup)
        session.commit()  # need to commit for changes to appear in database
        session.close()

    def addUserGroup(self, username, groupId):
        session = make_session()
        userGroup = UserGroup()
        userGroup.username = username
        userGroup.groupId = groupId
        session.add(userGroup)
        session.commit()  # need to commit for changes to appear in database
        session.close()
    # to be implemented in stage 2
    # def setAdmin(self, username, groupId):
    #     session = make_session()
    #     record = session.query(UserGroup)\
    #                     .filter(UserGroup.username == username,
    #                             UserGroup.groupId == groupId)\
    #                     .first()
    #     record.isAdmin = 1
    #     session.close()
    #
    # def isAdmin(self, username, groupId):
    #     session = make_session()
    #     record = session.query(UserGroup)\
    #                     .filter(UserGroup.username == username,
    #                             UserGroup.groupId == groupId)\
    #                     .first()
    #     session.close()
    #     return record.isAdmin

    def leaveGroup(self, username, groupId):
        session = make_session()
        record = session.query(UserGroup)\
                        .filter(UserGroup.username == username,
                                UserGroup.groupId == groupId)\
                        .first()
        session.delete(record)
        session.commit()  # need to commit for changes to appear in database
        session.close()

if __name__ == '__main__':
    k = UserGroup()
    k.createUserGroup('Munbodh21', 16)

