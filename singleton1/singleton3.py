class MetaSingleton(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super().__call__(*args, **kwargs)
        return cls._instance[cls]


class Logger(metaclass=MetaSingleton):
    pass


logger1 = Logger()
logger2 = Logger()
print(logger1, logger2)


class A(object):
    def my_func(self):
        pass

#! they are the same


def my_func():
    pass


B_name = "B"
B_parent = (object,)
B_methods = {"my_func": my_func()}


B = type(B_name, B_parent, B_methods)
