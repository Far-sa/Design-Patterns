from abc import ABCMeta, abstractmethod


#! Subject (Interface)


class Payment(metaclass=ABCMeta):

    @abstractmethod
    def do_pay(self):
        pass

#! Real Subject


class Bank(Payment):

    def __init__(self):
        self.card = None
        self.account = None

    def __get_account(self):
        self.account = self.card
        return self.account

    def __get_balance(self):
        print("Check mentioned account", self.__get_account())
        return False  # True

    def set_card(self, card):
        self.card = card

    def do_pay(self):
        if self.__get_balance():
            print("go into paying process")
            return True
        else:
            print("insufficient balance")
            return False

#! Proxy


class Card(Payment):

    def __init__(self):
        self.bank = Bank()

    def do_pay(self):
        card = input("Insert your Card,Checking id Card..")
        self.bank.set_card(card)
        return self.bank.do_pay()

#! Client


class Customer:

    def __init__(self):
        print("Customer :: I want to buy some clothes")
        self.card = Card()
        self.isPurchased = None

    def payment(self):
        self.isPurchased = self.card.do_pay()

    def __del__(self):
        if self.isPurchased:
            print("Purchase has done successfully")
        else:
            print("Your balance is not sufficient")


c = Customer()
c.payment()
