class Singleton():
    __instance = None

    def __init__(self):
        if not Singleton.__instance:
            print("We will be create an instance")
        else:
            print("Instance has already made", self.getInstance())

    #! get a func and make a procedure for a class
    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance
