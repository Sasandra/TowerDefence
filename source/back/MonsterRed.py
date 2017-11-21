from ..back import Monster


class MonsterGreen(Monster):
    def __init__(self):
        self.start_health = 5
        super(MonsterGreen, self).__init__(1, self.start_health, 5, (255, 0, 0))

    def increase_health(self):
        self.start_health += 1

    def decrease_health(self, amount):
        super(MonsterGreen, self).decrease_health(amount)

    def check_health(self):
        super(MonsterGreen, self).check_health()
