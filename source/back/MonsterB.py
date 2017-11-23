from ..back import Monster


class MonsterBlue(Monster.Monster):
    def __init__(self, x, y):
        self.start_health = 140
        super(MonsterBlue, self).__init__(5, self.start_health, 20, 'monster_blue', x, y)

    def increase_health(self):
        self.start_health += 3

    def decrease_health(self, amount):
        super(MonsterBlue, self).decrease_health(amount)

    def check_health(self):
        return super(MonsterBlue, self).check_health()

    def change_image(self):
        super(MonsterBlue, self).change_image()

    def level_up(self):
        super(MonsterBlue, self).level_up()
