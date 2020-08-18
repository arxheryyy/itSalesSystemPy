import computer


class laptop(computer):  # noqa
    def __init__(self, computerID, memory, storage, clockspeed):
        super().__init__(computerID, memory, storage, clockspeed)

        self.computerID = computerID
        self.memory = memory
        self.storage = storage
        self.clockspeed = clockspeed
