import datetime


def log_decorator(func):
    def wrapper(*args, **kwargs):
        date = datetime.datetime.now()
        value = func(*args, **kwargs)
        with open("log.txt", "a") as f:
            name = func.__name__
            f.write(
                f"function :{name} data : {date} returned:{value} args :{args} kwargs : {kwargs} \n")

        return value
    return wrapper


# my_decorator(say_hi)()


@log_decorator
def say_hi():
    print("Hey Puppet")


@log_decorator
def add(x, y):
    print("total:", x + y)
    return x + y


say_hi()
add(2, 3)
