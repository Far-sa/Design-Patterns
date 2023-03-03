
#! Facade
class EventManager():

    def __init__(self):
        print("EventManager:: Need to arrange sub systems")

    def arrange(self):
        self.presenter = Presenter()
        self.presenter.setPresentation()

        self.musicians = MusiciansGroup()
        self.musicians.setMusiciansGroup()

        self.caterer = Caterer()
        self.caterer.setCaterer()

        self.lecturer = Lecturer()
        self.lecturer.setLecturer()

#! Sub Systems


class Presenter():

    def __init__(self):
        print("When should i present!?")

    def setPresentation(self):
        print("Wednesday,2 hours")


class MusiciansGroup():

    def __init__(self):
        print("What kind of music do you need?")

    def setMusiciansGroup(self):
        print("Pop Rock,Local")


class Caterer():

    def __init__(self):
        print("What type of food and drink do you need?")

    def setCaterer(self):
        print("Pizza,Bear")


class Lecturer():

    def __init__(self):
        print("What type of lecture you will need?!")

    def setLecturer(self):
        print("About educational pattern in OOP")

#! Client


class Client():

    def __init__(self):
        print("Boss :: Lots of paper working must be done...")

    def ask_event_manager(self):
        print("Boss :: every task will be arranged")

        em = EventManager()
        em.arrange()

    def __del__(self):
        print("Boss :: I would appreciate about all the arrangement")


event = Client()
event.ask_event_manager()
