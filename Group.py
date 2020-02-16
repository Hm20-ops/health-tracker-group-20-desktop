from datetime import datetime
from enum import Enum
from User import User


class Group:
    def __init__(self, name, type, admin=[], members=[], common_goal=None):
        self.__id = id(self)
        self.__name = name
        GroupType = Enum('GroupType', 'OPEN RESTRICTED')
        self.__type = GroupType[type.upper()]
        self.__admin = admin
        self.__members = members
        self.__common_goal = common_goal

    def set_goal(self, goal):
        self.__common_goal = goal

    def invite(self, user):
        self.__members.append(user)

    def goal_archived(self):
        return self.__common_goal.date == datetime.now()

    def send_details(self, goal):
        pass

    def send_goal(self, goal):
        pass

    def accept_user(self, user):
        pass

    def is_admin(self, user):
        return self.__admin.contains(user)

    def kick_user(self, user):
        if user not in self.__members:
            raise ValueError('User not in the group')
        self.__members.remove(user)


def main():
    print()


if __name__ == '__main__':
    main()