import SuportedSports
import abstract_stadium
import Stadium
import SwimmingPool
import TenisCort
import PaintBallArena
from typing import List


class StadiumManager():
    """
    """
    sports = List[SuportedSports]
    stadiums = List[abstract_stadium]

    def add_stadium(self, stadium):
        self.sports.append(stadium)

    def find_all_stadiums_with_showers_more_than(self,number):
        stadiums_with_showers = list(filter(lambda x:x.number_of_showers > number,self.stadiums))
        print(stadiums_with_showers)
        return stadiums_with_showers

    def find_all_stdiums_with_capacity_more_than(self,count):
        stadiums_with_capacity = list(filter(lambda x:x.capacity > count,self.stadiums))
        return self.stadiums
