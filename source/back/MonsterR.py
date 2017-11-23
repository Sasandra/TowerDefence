from ..back import Monster


class MonsterRed(Monster.Monster):
    def __init__(self, x, y):
        self.start_health = 100
        super(MonsterRed, self).__init__(2, self.start_health, 5, 'monster_red.png', x, y)

    def increase_health(self):
        self.start_health += 1

    def decrease_health(self, amount):
        super(MonsterRed, self).decrease_health(amount)

    def check_health(self):
        return super(MonsterRed, self).check_health()
