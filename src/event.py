class Event:
    def __init__(self, time, identifier=-1):
        self.time = time
        self.id = identifier

    def __le__(self, other):
        return True if self.time <= other.time else False

    def __lt__(self, other):
        return True if self.time < other.time else False

    def __gt__(self, other):
        return not self.__le__(self, other)

    def __ge__(self, other):
        return not self.__lt__(self, other)
