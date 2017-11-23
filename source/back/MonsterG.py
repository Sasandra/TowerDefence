from ..back import Monster


class MonsterGreen(Monster.Monster):
    def __init__(self, x, y):
        self.start_health = 120
        super(MonsterGreen, self).__init__(3, self.start_health, 10, 'monster_green', x, y)

    def increase_health(self):
        self.start_health += 2

    def decrease_health(self, amount):
        super(MonsterGreen, self).decrease_health(amount)

    def check_health(self):
        return super(MonsterGreen, self).check_health()

    def change_image(self):
        super(MonsterGreen, self).change_image()

    def level_up(self):
        super(MonsterGreen, self).level_up()
