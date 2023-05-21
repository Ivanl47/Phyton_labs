import SuportedSports
import Stadium
import SwimmingPool
import TenisCort
import PaintBallArena
from typing import List


class StadiumManager():
    """
    """
    sports = List[SuportedSports]

    def add_stadium(self, stadium):
        self.sports.append(stadium)

    def find_all_stadiums_with_showers_more_than(self):
        stadiums_with_showers = list(filter(lambda ))
