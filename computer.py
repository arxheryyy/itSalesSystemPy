class computer:
    def __init__(self, computerID, memory, storage, clockspeed):
        self.computerID = computerID
        self.memory = memory
        self.storage = storage
        self.clockspeed = clockspeed


class laptop(computer):
    def __init__(self, computerID, memory, storage, clockspeed, weight):
        super().__init__(computerID, memory, storage, clockspeed)

        self.weight = weight


class desktop(computer):
    def __init__(self, computerID, memory, storage, clockspeed, monitor):
        super().__init__(computerID, memory, storage, clockspeed)

        self.monitor = monitor
