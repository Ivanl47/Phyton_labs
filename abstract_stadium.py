from abc import ABC, abstractmethod
import SuportedSports


class abstract_stadium(ABC):
    """
    Abstract Stadium
    Attributes:
        __name(str): - name of stadium
        __capacity(int): capacity of stadium
        __current_attendance(int): current attendance on stadium
        __number_of_showers(int): number of showers at the stadium
    """
    __name = ""
    __capacity = 0
    __current_attendance = 0
    __sports = [SuportedSports]
    __number_of_showers = 0

    @abstractmethod
    def get_supported_sports(self):
        """
        """