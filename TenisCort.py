import AbstractStadium
import SuportedSports


class TenisCort(AbstractStadium):
    """
    Class representing a Tenis cort.
    Attributes:
        name (str): The name of the tenis cort.
        capacity (int): The seating capacity of the tenis cort.
        current_attendance (int): The current number of attendees in the swimming pool.
        length_of_net (float): The length of net at the tenis cort
        sports (list): The list of supported sports
    """

    def __init__(self, __name="", __capacity=0, __current_attendance=0,__length_of_net=0 ,__sports=[SuportedSports],__number_of_showers=0):
        self.name = __name
        self.capacity = __capacity
        self.current_attendance = __current_attendance
        self.length_of_net = __length_of_net
        self.sports = __sports
        self.number_of_showers = __number_of_showers

    def get_supported_sports(self, sports):
        """
        """
        self.__sports.append(sports)
        return self.__sports
