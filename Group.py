

from datetime import datetime, date
from sqlalchemy import *
from sqlalchemy import Column
from ModelHandler import *


class Group(Base):
    __tablename__ = "Group"
    groupName = Column(String, nullable=False)
    groupId = Column(Integer, primary_key=True, autoincrement=True)
    groupType = Column(Enum('OPEN', 'Restricted'), nullable=False)
    completeGoalDate = Column(Date, nullable=False)

    # Group = relationship('Group', secondary='UserInGroups')#this seemed to cause crash
    @staticmethod
    def createGroup(groupName, groupType, completeGoalDate):
        session = make_session()
        group = Group()
        group.groupName = groupName
        group.groupType = groupType
        group.completeGoalDate = completeGoalDate
        session.add(group)
        session.commit()  # need to commit for changes to appear in database
        session.refresh(group)
        id = group.groupId
        session.close()
        return id

    def get_id_by_name(self, name):
        session = make_session()
        id = session.query(Group).filter(Group.groupName == name).first().groupId
        session.close()
        return id

    # @staticmethod
    # def get_all_group():
    #     #import CustomGoal
    #     session = make_session()
    #     # query FoodDictionary to fetch all rows
    #     data = session.query(Group).join(CustomGoal) \
    #         .with_entities(Group.groupName, CustomGoal.goal_description).all()
    #     session.close()
    #     return data

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

    Group.createGroup('FatBurner', 'OPEN', date_object)



if __name__ == '__main__':
    g = Group()
    print(g.createGroup('Group', 'OPEN', date.today()))

