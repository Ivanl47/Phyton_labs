import AbstractStadium
import SuportedSports


class PaintballArena(AbstractStadium):
    """
    Class representing a paintball arena.
    Attributes:
        name (str): The name of the arena.
        capacity (int): The seating capacity of the arena.
        current_attendance (int): The current number of attendees in the arena.
        number_of_covers (int): The number of covers at the arena.
        sports (list): The list of supported sports
    """
    def __init__(self, __name="", __capacity=0, __current_attendance=0, __number_of_covers=0, __sports=[SuportedSports],__number_of_showers=0):
        self.name = __name
        self.capacity = __capacity
        self.current_attendance = __current_attendance
        self.number_of_covers = __number_of_covers
        self.sports = __sports
        self.number_of_showers = __number_of_showers

    def get_supported_sports(self, sports):
        """
        """
        self.__sports.append(sports)
        return self.__sports
