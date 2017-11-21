from ..back import Monster


class MonsterBlue(Monster.Monster):
    def __init__(self, x, y):
        self.start_health = 15
        super(MonsterBlue, self).__init__(3, self.start_health, 15, 'monster_blue.png', x, y)

    def increase_health(self):
        self.start_health += 3

    def decrease_health(self, amount):
        super(MonsterBlue, self).decrease_health(amount)

    def check_health(self):
        return super(MonsterBlue, self).check_health()