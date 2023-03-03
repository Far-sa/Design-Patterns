import sys


def generate_text(path):
    myList = []
    with open(path) as file_handler:
        for line in file_handler:
            myList.append(line)
    return myList


def generate_text_generator(path):

    with open(path) as file_handler:
        for line in file_handler:
            yield line


value = generate_text_generator()
print(value.__next__())

print(sys.getsizeof(generate_text()))
print(sys.getsizeof(generate_text_generator()))
