from ..back import Monster


class MonsterBlue(Monster):
    def __init__(self):
        self.start_health = 15
        super(MonsterBlue, self).__init__(3, self.start_health, 15, (0, 0, 255))

    def increase_health(self):
        self.start_health += 3

    def decrease_health(self, amount):
        super(MonsterBlue, self).decrease_health(amount)

    def check_health(self):
        super(MonsterBlue, self).check_health()
