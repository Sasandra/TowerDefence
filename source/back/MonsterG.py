from ..back import Monster


class MonsterGreen(Monster.Monster):
    def __init__(self, x, y):
        self.start_health = 10
        super(MonsterGreen, self).__init__(2, self.start_health, 10, 'monster_green.png', x, y)

    def increase_health(self):
        self.start_health += 2

    def decrease_health(self, amount):
        super(MonsterGreen, self).decrease_health(amount)

    def check_health(self):
        return super(MonsterGreen, self).check_health()
