from abc import ABCMeta, abstractmethod

#! Travel Agency


class Travel(metaclass=ABCMeta):

    @abstractmethod
    def first_day(self):
        pass

    @abstractmethod
    def second_day(self):
        pass

    @abstractmethod
    def third_day(self):
        pass

    @abstractmethod
    def last_day(self):
        pass

    #! template method
    def travel_plan(self):
        self.first_day()
        self.second_day()
        self.third_day()
        self.last_day()


#! Concrete class

class AbroadTravel(Travel):

    def first_day(self):
        print("visit to the central sight")

    def second_day(self):
        print("visit to the ancient sight")

    def third_day(self):
        print("visit to the shopping center")

    def last_day(self):
        print("stay at the hotel")


class InsideTravel(Travel):

    def first_day(self):
        print("visit to the rural center")

    def second_day(self):
        print("visit to the sight seen center")

    def third_day(self):
        print("visit to the shopping center")

    def last_day(self):
        print("stay at the hotel")


#! Client


class TravelAgency():

    def make_tour(self):
        destination = input("Please select the destination..? ")
        if destination == "AbroadTravel":
            self.trip = AbroadTravel()
            self.trip.travel_plan()
        if destination == "InsideTravel":
            self.trip = InsideTravel()
            self.trip.travel_plan()


TravelAgency().make_tour()
