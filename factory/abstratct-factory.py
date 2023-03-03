from abc import ABCMeta, abstractmethod


#! Abstract Factory
class CoffeeFactory(metaclass=ABCMeta):

    @abstractmethod
    def create_coffee_with_milk(self):
        pass

    @abstractmethod
    def create_coffee_without_milk(self):
        pass

    # @abstractmethod
    # def cold_coffee(self):
    #     pass

    # @abstractmethod
    # def hot_coffee(self):
    #     pass


#! Concrete Factory
class ItalianCoffeeFactory(CoffeeFactory):

    def create_coffee_with_milk(self):
        return ItalianCappuccino()

    def create_coffee_without_milk(self):
        return ItalianEspresso()


class FrenchCoffeeFactory(CoffeeFactory):

    def create_coffee_with_milk(self):
        return FrenchCappuccino()

    def create_coffee_without_milk(self):
        return FrenchEspresso()


#! Abstract Product

class CoffeeWithoutMilk(metaclass=ABCMeta):

    @abstractmethod
    def prepare(self, CoffeeWithoutMilk):
        pass


class CoffeeWithMilk(metaclass=ABCMeta):

    @abstractmethod
    def serve(self, CoffeeWithoutMilk):
        pass


#! Concrete Product
class ItalianCappuccino(CoffeeWithMilk):

    def serve(self, CoffeeWithoutMilk):
        print(type(self).__name__, "Is Served")

        print(type(self).__name__, "Is Served")


class ItalianEspresso(CoffeeWithoutMilk):

    def prepare(self):
        print("Coffee is Prepared!", type(self).__name__)


class FrenchEspresso(CoffeeWithoutMilk):

    def prepare(self):
        print("Coffee is Prepared!", type(self).__name__)


class FrenchCappuccino(CoffeeWithMilk):

    def serve(self, CoffeeWithoutMilk):
        print(type(self).__name__, "Is Served with Cow's Milk")


#! Client
class CoffeeStore:

    def __init__(self):
        pass

    def make_coffee(self):
        for factory in [ItalianCoffeeFactory(), FrenchCoffeeFactory()]:
            self.factory = factory
            self.CoffeeWithoutMilk = self.factory.create_coffee_without_milk()
            self.CoffeeWithMilk = self.factory.create_coffee_with_milk()
            self.CoffeeWithoutMilk.prepare()
            # self.CoffeeWithMilk.serve()


coffee = CoffeeStore()
coffee.make_coffee()
