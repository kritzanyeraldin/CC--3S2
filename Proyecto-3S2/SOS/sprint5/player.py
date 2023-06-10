class player:
    def __init__(self, name):
        self.name=name

    def type(self):
        raise NotImplementedError('Not implement')


class HumanPlayer(player):
    def __init__(self, name):
        super().__init__(name)

    def type(self):
        return 'Human'

class ComputerPlayer(player):
    def __init__(self, name):
        super().__init__(name)

    def type(self):
        return 'Computer'