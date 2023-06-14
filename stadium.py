from abstract_stadium import AbstractStadium
import not_enough_seats_exeption
from stadium_manager import StadiumManager


class Stadium(AbstractStadium):
    """
    Class representing a stadium.

    Attributes:
        __name (str): The name of the stadium.
        __capacity (int): The seating capacity of the stadium.
        __current_attendance (int): The current number of attendees in the stadium.
        __home_team (str): The home team playing at the stadium.
        __away_team (str): The away team playing against the home team.
    """

    def __init__(self,
                 __name="",
                 __current_attendance=0,
                 __capacity=0,
                 __home_team="",
                 __away_team="",
                 __sports=[],
                 __number_of_showers=0):
        """
        Initializes an instance of the Stadium class with the specified attributes.

        Parameters:
            __name (str): The name of the stadium.
            __capacity (int): The seating capacity of the stadium.
            __current_attendance (int): The current number of attendees in the stadium.
            __home_team (str): The home team playing at the stadium.
            __away_team (str): The away team playing against the home team.
            __sports (list): The list of supported sports
        """
        self.__name = __name
        self.__capacity = __capacity
        self.__current_attendance = __current_attendance
        self.__home_team = __home_team
        self.__away_team = __away_team
        self.__sports = __sports
        self.__number_of_showers = __number_of_showers

    @logged
    def add_attendance(self, count):
        """
        Adds the specified number of attendees to the current attendance at the stadium.

        Parameters:
            count (int): The number of attendees to add.
        """
        self.__current_attendance += count
        if self.__current_attendance > self.__capacity:
            raise not_enough_seats_exeption
            # excess = self.__current_attendance - self.__capacity
            # self.__current_attendance = self.__capacity
            # print(
            #     f" in the stadium. Excess: {excess}. Attendance changed to {self.__current_attendance}.")

    def decrease_attendance(self):
        """
        Decreases the current attendance at the stadium by 100.
        """
        self.__current_attendance -= 100
        if self.__current_attendance < 0:
            self.__current_attendance = 0
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

    def get_supported_sports(self, sports):
            """
            """
            self.__sports.append(sports)
            return self.__sports
