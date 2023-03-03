
#! Function as Object

from time import sleep


def func():
    sleep(1000)
    return 1 + 1


def test_func():
    return 2


# use as an object
temp = func
func = test_func

# main.py
print("Function result : ", func())
