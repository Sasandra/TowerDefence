from ..back import Monster
from ..texts import constatnts


class MonsterRed(Monster.Monster):
    def __init__(self, x, y, direction_):
        self.start_health = constatnts.RED_MONSTER_START_HEALTH
        super(MonsterRed, self).__init__(constatnts.RED_MONSTER_SPEED, self.start_health, constatnts.RED_MONSTER_PRIZE,
                                         constatnts.RED_MONSTER_IMG, x, y, direction_)

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

    def change_direction_image(self):
        super(MonsterRed, self).change_direction_image()
