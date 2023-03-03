class Book():
    _shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj


a1 = Book()
a2 = Book()
a3 = Book()

a1.x = "200"


print("A1 instance :", a1)
print("A1 instance :", a2)
print("A1 instance :", a3)

print("obj state a1 :", a1.__dict__)
print("obj state a2 :", a2.__dict__)
print("obj state a3 :", a3.__dict__)
