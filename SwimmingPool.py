import abstract_stadium
import SuportedSports


class SwimmingPool(abstract_stadium):
    """
    Class representing a swimming pool.
    Attributes:
        name (str): The name of the swimming pool.
        capacity (int): The seating capacity of the swimming pool.
        current_attendance (int): The current number of attendees in the swimming pool.
        number_of_showers (int): The number of showers at the swimming pool.
        pool_volume_in_liters (float): The volume of swimming poll.
        number_of_members (int): The max capacity of members in team.
        sports (list): The list of supported sports
    """

    def __init__(self,
                 __name: str = "",
                 __capacity: int = 0,
                 __current_attendance: int = 0,
                 __number_of_showers: int = 0,
                 __pool_volume_in_liters: float = 0,
                 __number_of_members: int = 0,
                 __sports: list[SuportedSports] = ()
                 ):
        self.name = __name
        self.capacity = __capacity
        self.current_attendance = __current_attendance
        self.number_of_showers = __number_of_showers
        self.pool_volume_in_liters = __pool_volume_in_liters
        self.number_of_members = __number_of_members
        self.sports = __sports

    def get_supported_sports(self,sports):
        """
        """
        self.__sports.append(sports)
        return self.__sports


