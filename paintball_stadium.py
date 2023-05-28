import abstract_stadium
import SuportedSports


class PaintballArena(abstract_stadium):
    """
    Class representing a paintball arena.
    Attributes:
        name (str): The name of the arena.
        capacity (int): The seating capacity of the arena.
        current_attendance (int): The current number of attendees in the arena.
        number_of_covers (int): The number of covers at the arena.
        sports (list): The list of supported sports
    """
    def __init__(self, name="", capacity=0, current_attendance=0, number_of_covers=0, sports=[SuportedSports], number_of_showers=0):
        self._name = name
        self._capacity = capacity
        self._current_attendance = current_attendance
        self._number_of_covers = number_of_covers
        self._sports = sports
        self._number_of_showers = number_of_showers

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    @property
    def current_attendance(self):
        return self._current_attendance

    @current_attendance.setter
    def current_attendance(self, current_attendance):
        self._current_attendance = current_attendance

    @property
    def number_of_covers(self):
        return self._number_of_covers

    @number_of_covers.setter
    def number_of_covers(self, number_of_covers):
        self._number_of_covers = number_of_covers

    @property
    def sports(self):
        return self._sports

    @sports.setter
    def sports(self, sports):
        self._sports = sports

    @property
    def number_of_showers(self):
        return self._number_of_showers

    @number_of_showers.setter
    def number_of_showers(self, number_of_showers):
        self._number_of_showers = number_of_showers

    def get_supported_sports(self, sports):
        self._sports.append(sports)
        return self._sports

