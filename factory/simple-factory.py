from abc import ABCMeta, abstractmethod


class Book(metaclass=ABCMeta):

    @abstractmethod
    def get_pages(self):
        pass


class The_Teo(Book):
    def get_pages(self):
        print("500")


class The_mashol(Book):
    def get_pages(self):
        print("300")

#! Factory


class PublicationFactory():

    def Book_publisher(self, obj):
        return eval(obj)().get_pages()


#! Client
if __name__ == "__main__":
    book1 = PublicationFactory()
    book = input("Which book do you want to pick? The_Teo / The_Mashol? ")
    book1.Book_publisher(book)
