class Stadium:

    def __init__(self, __name, __capacity, __current_attandies, __home_team, __away_team):
        self.__name = __name
        self.__capacity = __capacity
        self.__current_attandies = __current_attandies
        self.__home_team = __home_team
        self.__away_team = __away_team
        @property
        def model(self):
            return self.__model
        @model.setter
        def model(self,__name):
            return self.__model

        @model.setter
        def model(self, __capacity):
            return self.__model@model.setter
        @model.setter
        def model(self,__current_attandies):
            return self.__model

        @model.setter
        def model(self, __home_team):
            return self.__model

        @model.setter
        def model(self, __away_team):
            return self.__model



    def add_attandies(self, count):
        self.__current_attandies += count
        if self.__current_attandies > self.__capacity:
            excess = self.__current_attandies - self.__capacity
            self.__current_attandies = self.__capacity
            print("замало місць на стадіоні, надлишок:", excess,".", "кількість глядачів змінено на ", self.__current_attandies)

    def decrease_attendance(self):
        self.__current_attandies -= 100
        if self.__current_attandies < 0:
            self.__current_attandies = 0
            print("кількість глядачів не може бути відємною, кількість глядачів змінена на 0")

    def change___home_team(self, team_name):
        self.__home_team = team_name

    def change___away_team(self, team_name):
        self.__away_team = team_name

