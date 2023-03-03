from abc import ABCMeta, abstractmethod


class Section(metaclass=ABCMeta):

    @abstractmethod
    def describe(self):
        pass

#! Sections


class PersonalInfoSection(Section):

    def describe(self):
        print("This is a personal info section")


class AlbumSection(Section):

    def describe(self):
        print("This is a album info section")


class PatentSection(Section):

    def describe(self):
        print("This is a patent info section")


class PublicSection(Section):

    def describe(self):
        print("This is a public info section")

#! Creator (factory)


class Profile(metaclass=ABCMeta):

    def __init__(self):
        self.sections = []
        self.createProfile()

    @abstractmethod
    def createProfile(self):
        pass

    def get_sections(self):
        return self.sections

    def add_sections(self, section):
        return self.sections.append(section)


class LinkedIn(Profile):

    def createProfile(self):
        self.add_sections(PersonalInfoSection)
        self.add_sections(AlbumSection())
        self.add_sections(PublicSection())


class Google(Profile):

    def create_profile(self):
        self.add_sections(PersonalInfoSection())
        self.add_sections(PublicSection())
        self.add_sections(AlbumSection())
        self.get_sections()


#! Client
if __name__ == '__main__':
    profile_input = input("Which one do you want? LinkedIn or Google  !")
    profile = eval(profile_input)
    print("Your success profile is :", type(profile).__name__)
