from enum import Enum
import datetime
from Group import Group
from GoalInterface import GoalInterface


class User:
    def __init__(self, username, name, email, dob, password, gender, age, weight, height):
        #load account details
        self.__username = username
        self.__email = email
        self.__password = password
        # load user details
        self.__name = name
        self.__dob = datetime.datetime.strptime(dob, "%d/%m/%Y").date()
        Gender = Enum('Gender', 'Male Female PREFER_NOT_TO_SAY')
        self.__gender = Gender[gender.upper()]
        self.__age = age
        self.__weight = weight
        self.__height = height
        self.__goals = []
        self.__groups = []
        print('\n'.join("%s: %s" % item for item in vars(self).items()))

    def create_group(self):
        """

        """
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

def main():
    user = User('user', 'tim', 't123@gmail.com', '04/3/1990', 'password', 'male', 30, 60, 180)

if __name__ == '__main__':
    main()