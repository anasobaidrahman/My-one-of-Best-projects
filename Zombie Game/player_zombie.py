class player():

    def __init__(self,name):
        self.name=name
        self.__lives=3
        self.__level=1
        self.score=0

    @property
    def lives(self):  # getter
        return self.__lives

    @lives.setter
    def lives(self, value):  # setter
        if value >= 0:
            self.__lives = value
        else:
            print("Lives can't be negative.")
            self.__lives = 0
    @property
    def level(self):
        return self.__level
    @level.setter
    def level(self,level):
        if level>=1:
            delta=level-self.__level
            self.score+= delta * 100
            self.__level=level
        else:
            print('level cannot be less than one')


    def __str__(self):
        return f'Name:{self.name},Level:{self.level},lives:{self.lives},Score:{self.score}'