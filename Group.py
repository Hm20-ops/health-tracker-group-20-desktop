from enum import Enum
from User import User

class Group:
    def __init__(self, name, type, admin=User, members=User(), common_goal=None):
        self.__id = id(self)
        self.__name = name
        GroupType = Enum('GroupType', 'OPEN RESTRICTED')
        self.__type = GroupType[type.upper()]
        self.__admin = admin
        self.__members = members
        self.__common_goal = common_goal

def main():
    print()
if __name__ == '__main__':
    main()