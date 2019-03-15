class Event:
    def __init__(self, time, nature):
        self.time = time
        self.nature = nature
        self.client = None

    def __le__(self, other):
        return True if self.time <= other.time else False

    def __lt__(self, other):
        return True if self.time < other.time else False

    def __gt__(self, other):
        return not self.__le__(self, other)

    def __ge__(self, other):
        return not self.__lt__(self, other)

    def pair(self, client):
        self.client = client
        