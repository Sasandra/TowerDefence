from ..back import Monster


class MonsterRed(Monster.Monster):
    def __init__(self, x, y):
        self.start_health = 100
        super(MonsterRed, self).__init__(2, self.start_health, 5, 'monster_red', x, y)

    def increase_health(self):
        self.start_health += 1

    def decrease_health(self, amount):
        super(MonsterRed, self).decrease_health(amount)

    def check_health(self):
        return super(MonsterRed, self).check_health()

    def change_image(self):
        super(MonsterRed, self).change_image()

    def level_up(self):
        super(MonsterRed, self).level_up()

    def check_if_collidepoint(self, pos):
        return super(MonsterRed, self).check_if_collidepoint(pos)

    def return_description(self):
        return super(MonsterRed, self).return_description()

    def check_if_clicked(self):
        return super(MonsterRed, self).check_if_clicked()
