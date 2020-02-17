class Cardio:
    __name = ""
    __duration = 0
    __baseCalorie = 0
    def __init__(self,name,duration,baseCalorie):
        self.__name = name
        self.__baseCalorie=baseCalorie
        self.__duration=duration

    def get_name(self):
        return self.__name
    def get_duration(self):
        return self.__duration
    def get_baseCalorie(self):
        return self.__baseCalorie


    def set_name(self, name):
        self.__name = name

    def set_duration(self, duration):
        self.__duration = duration
    def set_x(self, baseCalorie):
        self.__baseCalorie = baseCalorie

def main():
    cardio = Cardio(0,0,0)
    cardio.set_duration(50)
    print(cardio.get_duration())




if __name__ == "__main__":
    main()
