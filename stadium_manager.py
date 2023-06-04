import SuportedSports
import abstract_stadium
import stadium
import SwimmingPool
import TenisCort
import paintball_stadium
from typing import List
import logging


class StadiumManager():
    """
    """
    sports = List[SuportedSports]
    stadiums = List[abstract_stadium]

    def add_stadium(self, stadium):
        self.sports.append(stadium)

    def logged(exception, mode):
        def decorator(func):
            def wrapper(*args, **kwargs):
                try:
                    return func(*args, **kwargs)
                except exception as e:
                    if mode == "console":
                        logging.basicConfig(level=logging.INFO)
                        logging.error(f"Exception occurred: {e}")
                    elif mode == "file":
                        logging.basicConfig(filename="log.txt", level=logging.INFO)
                        logging.error(f"Exception occurred: {e}")
                    else:
                        raise ValueError("Invalid logging mode.")

            return wrapper

        return decorator

    def find_all_stadiums_with_showers_more_than(self,number):
        stadiums_with_showers = all(self.number_of_showers > number for self.number_of_showers in self.stadiums)
        #list(filter(lambda x:x.number_of_showers > number,self.stadiums))
        print(stadiums_with_showers)
        return stadiums_with_showers

    def find_all_stdiums_with_capacity_more_than(self,count):
        stadiums_with_capacity = list(filter(lambda x:x.capacity > count,self.stadiums))
        return stadiums_with_capacity

    def __len__(self):
        return len(self.stadiums)

    def __getitem__(self, index):
        return self.sports[index]

    def __iter__(self):
        return iter(self.sports)

    def comprehension_method(self,sports):
        results = [f'{obj} - {obj.get_supported_sports()}' for obj in zip(sports, [obj.get_supported_sports() for obj in sports])]


    def enumerate_method(self, sports):
        for index, value in enumerate(sports):
            print(f"Index: {index}, Value: {value}")
