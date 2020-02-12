from enum import Enum
import datetime

class User:
    def __init__(self, username, name, email, dob, password, gender, age, weight, height):
        #load account details
        self.__username = username
        self.__email = email
        self.__password = password
        # load user details
        self.__name = name
        self.__dob = datetime.datetime.strptime(dob, "%d/%m/%Y").date()
        Gender = Enum('Gender', 'Male Female')
        self.__gender = Gender[gender.upper()]
        self.__age = age
        self.__weight = weight
        self.__height = height
        self.__goals = None
        self.__groups = None
        print('\n'.join("%s: %s" % item for item in vars(self).items()))

def main():
    user = User('user', 'tim', 't123@gmail.com', '04/3/1990', 'password', 'male', 30, 60, 180)

if __name__ == '__main__':
    main()