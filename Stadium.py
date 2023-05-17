class Stadium:
    """
    Class representing a stadium.

    Attributes:
        __name (str): The name of the stadium.
        __capacity (int): The seating capacity of the stadium.
        __current_attandies (int): The current number of attendees in the stadium.
        __home_team (str): The home team playing at the stadium.
        __away_team (str): The away team playing against the home team.
    """

    instance = None

    @staticmethod
    def get_instance():
        """
        Get the instance of the Stadium class.

        Returns:
            Stadium: The instance of the Stadium class.
        """
        if Stadium.instance is None:
            Stadium.instance = Stadium()
        return Stadium.instance

    def __init__(self, __name="", __capacity=0, __current_attandies=0, __home_team="", __away_team=""):
        """
        Initializes an instance of the Stadium class with the specified attributes.

        Parameters:
            __name (str): The name of the stadium.
            __capacity (int): The seating capacity of the stadium.
            __current_attandies (int): The current number of attendees in the stadium.
            __home_team (str): The home team playing at the stadium.
            __away_team (str): The away team playing against the home team.
        """
        self.__name = __name
        self.__capacity = __capacity
        self.__current_attandies = __current_attandies
        self.__home_team = __home_team
        self.__away_team = __away_team

    def add_attandies(self, count):
        """
        Adds the specified number of attendees to the current attendance at the stadium.

        Parameters:
            count (int): The number of attendees to add.
        """
        self.__current_attandies += count
        if self.__current_attandies > self.__capacity:
            excess = self.__current_attandies - self.__capacity
            self.__current_attandies = self.__capacity
            print(
                f"Not enough seats in the stadium. Excess: {excess}. Attendance changed to {self.__current_attandies}.")

    def decrease_attendance(self):
        """
        Decreases the current attendance at the stadium by 100.
        """
        self.__current_attandies -= 100
        if self.__current_attandies < 0:
            self.__current_attandies = 0
            print("Attendance cannot be negative. Attendance changed to 0.")

    def change___home_team(self, team_name):
        """
        Changes the home team to the specified team.

        Parameters:
            team_name (str): The name of the new home team.
        """
        self.__home_team = team_name

    def change___away_team(self, team_name):
        """
        Changes the away team to the specified team.

        Parameters:
            team_name (str): The name of the new away team.
        """
        self.__away_team = team_name
