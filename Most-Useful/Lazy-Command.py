from time import sleep


class LazyCommand:
    def __init__(self, command, *args, **kwargs):
        self.command = command
        self.args = args
        self.kwargs = kwargs

    def __call__(self):
        return self.command(*self.args, **self.kwargs)


def get_results(*, lazy: bool = False):
    if lazy:
        return LazyCommand(
            command=get_results,
            lazy=False
        )

    sleep(1000)
    return 1 + 1


def main():
    results = get_results(lazy=True)

    if 10 > 5:
        print("Hey Done!")
    else:
        print(2548978321)

    return results()


main()
