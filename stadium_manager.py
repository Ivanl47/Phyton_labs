import SuportedSports
import abstract_stadium
import stadium
import SwimmingPool
import TenisCort
import paintball_stadium
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

    def __len__(self):
        return len(self.stadiums)

    def __getitem__(self, index):
        return self.sports[index]

    def __iter__(self):
        return iter(self.sports)
