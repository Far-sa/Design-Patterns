from abc import ABCMeta, abstractmethod


class Section(metaclass=ABCMeta):

    @abstractmethod
    def describe(self):
        pass


class PersonalSection(Section):

    def describe(self):
        print("Private Section")


class AlbumSection(Section):

    def describe(self):
        print("Album Section")


class PatentSection(Section):

    def describe(self):
        print("Patent Section")


class PublicSection(Section):

    def describe(self):
        print("Public Section")


class Profile(metaclass=ABCMeta):

    def __init__(self):
        self.sections = []
        self.create_profile()

    @abstractmethod
    def create_profile(self):
        pass

    def get_sections(self):
        return self.sections

    def add_section(self, section):
        return self.sections.append(section)


class Google(Profile):

    def create_profile(self):
        self.add_section(PersonalSection())
        self.add_section(PublicSection())
        self.get_sections()


class LinkedIn(Profile):

    def create_profile(self):
        self.add_section(PersonalSection())
        self.add_section(AlbumSection())
        self.add_section(PatentSection())


if __name__ == '__main__':
    profile_input = input(
        "Select your Profile? -> LinkedIn  / Google ? ")
    profile = eval(profile_input)()
    print("Your Profile is: ", type(profile).__name__)
