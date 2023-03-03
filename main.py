from singleton1 import singleton1
from singleton1.singleton1 import Logger

from singleton1.main import SingletonObject


log_obj = Logger("file.txt")
log_obj.critical("this is an critical error")

obj1 = SingletonObject()
obj1.file_name = "log1.txt"
obj1.critical("this is an critical message")
print("obj1:", obj1)

obj2 = SingletonObject()
obj2.file_name = "log1.txt"
obj2.warning("this is an warning message")
print("obj1:", obj2)
print("obj1:", obj1)


# try:
#     a = 1/0
# except:
#     singleton1.error_log_messages("something goes wrong")
#     singleton1.warning_log_messages("something goes wrong")
